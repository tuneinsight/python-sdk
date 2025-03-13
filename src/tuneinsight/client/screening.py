"""Classes and utilities to screen a dataset."""

from typing import List, Optional, Union

import attr
import pandas as pd

from tuneinsight.client.diapason import Diapason
from tuneinsight.client.datasource import DataSource
from tuneinsight.client.validation import validate_response

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import value_if_unset
from tuneinsight.api.sdk.api.api_datasource import (
    get_screening_session,
    post_screening_session,
    patch_screening_session,
    delete_screening_session,
    load_screening_data,
    export_screened_data,
)


@attr.s(auto_attribs=True)
class ScreenedDataset:
    """The result of a screening operation."""

    metadata: models.ScreeningMetadata
    data: List[models.ScreenedRow]

    def to_pandas(self) -> pd.DataFrame:
        """Restructures the screened dataset result as a pandas DataFrame for later analysis."""
        data_columns = [c.name for c in self.metadata.columns]
        columns = (
            list(map(lambda x: f"{x} (raw)", data_columns))
            + list(map(lambda x: f"{x} (screened)", data_columns))
            + ["screened", "reason"]
        )
        data = [
            row.data + row.screened_data + [row.screened, row.reason]
            for row in self.data
        ]
        df = pd.DataFrame(data, columns=columns).map(lambda x: value_if_unset(x, ""))
        df["screened"] = df["screened"] == True  # pylint: disable=singleton-comparison
        return df


class ScreeningSession:
    """
    A screening session that allows users to interactively edit a dataset.

    In a screening session, an authorized user iteratively adds screening operations to
    a dataset in order to prepare it for computations. This involves filtering out and/or
    editing records that are not properly formatted or otherwise erroneous.

    A screening session is attached to a datasource (and query), and defined by a list
    of operations that filter and transform the data (result of the query on the datasource).

    The `load` operation queries the data and applies the current set of operations, and
    returns the result of the query (raw) as well as the transformed dataset (screened).

    Once the screening is completed, the `export` operation takes a snapshot of the screened
    dataset and stores it as a new datasource. This datasource can then be used in computations.
    """

    @classmethod
    def new(
        cls, client: Diapason, definition: models.ScreeningSessionDefinition
    ) -> "ScreeningSession":
        """Create a new screening session.

        Args:
            client (Diapason): the client used to interact with the instance.
            definition (models.ScreeningSessionDefinition): the definition of the screening session.

        """
        resp = post_screening_session.sync_detailed(
            client=client.client, json_body=definition
        )
        validate_response(resp)
        return cls(client, unique_id=resp.parsed.id)

    def __init__(self, client: Diapason, unique_id: str):
        """Accesses a screening session identified by a unique identifier.

        Args:
            client (Diapason): the connector client.
            unique_id (str): the unique identifier of this screening session.
        """
        self.client = client.client
        self.unique_id = unique_id
        self.model: models.ScreeningSession = self._get_model()

    ## Internal handlers.

    def _get_model(self):
        resp = get_screening_session.sync_detailed(self.unique_id, client=self.client)
        validate_response(resp)
        return resp.parsed

    def _patch(self, model: models.ScreeningSessionDefinition):
        """Patches the definition of the screening session.

        Args:
            model (models.ScreeningSessionDefinition): API models with fields to change.
        """
        resp = patch_screening_session.sync_detailed(
            self.unique_id, client=self.client, json_body=model
        )
        validate_response(resp)
        self.model = resp.parsed

    ## High-level methods to handle a session.

    def set_datasource(self, ds: Union[str, DataSource]):
        """Sets the datasource of this screening session.

        Args:
            ds (Union[str, DataSource]): either a Datasource object, or the unique ID of the datasource.
        """
        if isinstance(ds, DataSource):
            ds = ds.get_id()
        self._patch(models.ScreeningSessionDefinition(data_source_id=ds))

    def set_query(self, query: models.DataSourceQuery):
        """Sets the datasource query for this screening session.

        Args:
            query (QueryBuilder): the query as an API model.
        """
        self._patch(models.ScreeningSessionDefinition(query=query))

    def load(self) -> ScreenedDataset:
        """
        Loads, queries, and screens the retrieved dataset in the screen session.

        This returns the result of the operation, a screened dataset.
        """
        resp = load_screening_data.sync_detailed(self.unique_id, client=self.client)
        validate_response(resp)
        self.model = resp.parsed
        return ScreenedDataset(metadata=self.model.metadata, data=self.model.data)

    def delete(self):
        """Deletes this screening session."""
        resp = delete_screening_session.sync_detailed(
            self.unique_id, client=self.client
        )
        validate_response(resp)

    def export(self, datasource_name: str) -> DataSource:
        """Exports the screening session to a datasource.

        Args:
            datasource_name (str): name of the datasource.

        Returns:
            DataSource: the datasource object exported from the session.
        """
        resp = export_screened_data.sync_detailed(
            self.unique_id, data_source_name=datasource_name, client=self.client
        )
        validate_response(resp)
        return DataSource(resp.parsed, client=self.client)

    ## Handling operations on this session.

    def _set_operations(self, operations: models.ScreeningOperation):
        self._patch(models.ScreeningSessionDefinition(operations=operations))

    def add_operation(self, operation: models.ScreeningOperation):
        """Adds a screening operation to this session.

        Args:
            operation (models.ScreeningOperation): the operation to add.
        """
        operations = value_if_unset(self.model.operations, [])
        operation.enabled = True
        operations.append(operation)
        self._set_operations(operations)

    def remove_operation(self, index: Optional[int] = -1, hard: Optional[bool] = False):
        """Removes a screening operation from this session.

        Args:
            index (Optional[int], optional): the index of the operation in the current operations list, as a valid
                index for that list. Defaults to -1 (last operation added).
            hard (Optional[bool], optional): whether to disable (False, default) the operation but still keep it in
                the list, or hard remove it from the list.
        """
        operations = value_if_unset(self.model.operations, [])
        n_op = len(operations)
        if not n_op:
            raise ValueError("No operation to remove.")
        if index < -n_op or index >= n_op:
            raise IndexError(
                f"Invalid index {index} (should be in [-{n_op}, {n_op-1}])"
            )
        # Either hard remove the operation, or temporarily disable it.
        if hard:
            del operations[index]
        else:
            operations[index].enabled = False
        self._set_operations(operations)

    def remove_rows(self, rows: List[int]) -> "ScreeningSession":
        """Adds a screening operation that removes specific rows in the data.

        Args:
            rows (List[int]): the list of indices (in the original data) or rows to remove

        Returns:
            self: this object (to chain operations).
        """
        self.add_operation(models.ScreeningOperation(rows=rows, remove=True))
        return self

    def edit_value(self, row: int, column: str, value: str) -> "ScreeningSession":
        """Adds a screening operation that edits a specific entry in the data.

        Args:
            row (int): index of the row in the original data.
            column (str): the name of the column.
            value (str): the value to set.

        Returns:
            self: this object (to chain operations).
        """
        self.add_operation(
            models.ScreeningOperation(columns=[column], rows=[row], replace_with=value)
        )
        return self

    def remove_outliers(
        self,
        columns: Union[str, List[str]],
        threshold: float,
        replace_with: Optional[str] = None,
    ) -> "ScreeningSession":
        """Adds a screening operation that removes outliers in selected columns.

        Args:
            columns (Union[str, List[str]]): The column(s) from which outliers are removed.
            threshold (float): the threshold (multiplicative of stddev) to define an outlier.
            replace_with (Optional[str], optional): if set, outlier records are not removed,
                but the outliers are replaced with this value. Defaults to None.

        Returns:
            self: this object (to chain operations).
        """
        if isinstance(columns, str):
            columns = [columns]
        self.add_operation(
            models.ScreeningOperation(
                columns=columns, outlier_threshold=threshold, replace_with=replace_with
            ),
        )
        return self

    def filter_empty(
        self, columns: Union[str, List[str]], replace_with: Optional[str] = None
    ) -> "ScreeningSession":
        """Adds a screeening operation that filters rows with empty values.

        Args:
            columns (Union[str, List[str]]): The column(s) where to look for empty cells.
            replace_with (Optional[str], optional): if set, rows with missing values are not
                removed, but the empty values are replaced with this value. Defaults to None.

        Returns:
            self: this object (to chain operations).
        """
        if isinstance(columns, str):
            columns = [columns]
        self.add_operation(
            models.ScreeningOperation(
                columns=columns, non_empty=True, replace_with=replace_with
            )
        )
        return self

    def filter_non_numeric(
        self, columns: Union[str, List[str]], replace_with: Optional[str] = None
    ) -> "ScreeningSession":
        """Adds a screening operation that filters out rows with non-numeric values.

        Args:
            columns (Union[str, List[str]]): The column(s) where to look for (non-)numeric values.
            replace_with (Optional[str], optional): if set, rows with non-numeric values are not
                removed but the invalid values are replaced with this value. Defaults to None.

        Returns:
            self: this object (to chain operations).
        """
        if isinstance(columns, str):
            columns = [columns]
        self.add_operation(
            models.ScreeningOperation(
                columns=columns, numeric=True, replace_with=replace_with
            )
        )
        return self

    def autocorrect_dates(self, columns: Union[str, List[str]]) -> "ScreeningSession":
        """Adds a screening operation that auto-correct poorly formatted dates.

        Args:
            columns (Union[str, List[str]]): The column(s) where to autocorrect dates.

        Returns:
            self: this object (to chain operations).
        """
        if isinstance(columns, str):
            columns = [columns]
        self.add_operation(
            models.ScreeningOperation(columns=columns, auto_correct_dates=True)
        )
        return self

    def filter_invalid_dates(
        self, columns: Union[str, List[str]], replace_with: Optional[str] = None
    ) -> "ScreeningSession":
        """Adds a screening operation that filters invalid dates.

        Args:
            columns (Union[str, List[str]]): The column(s) where to look for dates.
            replace_with (Optional[str], optional): if set, rows with invalid dates are not
                removed, but the invalid dates are replaced with this value. Defaults to None.

        Returns:
            self: this object (to chain operations).
        """
        if isinstance(columns, str):
            columns = [columns]
        self.add_operation(
            models.ScreeningOperation(
                columns=columns, filter_invalid_dates=True, replace_with=replace_with
            )
        )
        return self
