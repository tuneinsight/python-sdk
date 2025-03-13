"""Classes defining dataset schemas to constrain acceptable data formats."""

from typing import Dict, List, Any

# from tuneinsight.client import DataSource
from tuneinsight.client.validation import validate_response
from tuneinsight.utils.display import Renderer

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_set, UNSET, value_if_unset
from tuneinsight.api.sdk.api.api_datasource import post_data_source_infer_schema


class DatasetSchema:
    """
    A user-defined dataset schema that constrains the structure of input datasets.

    Schemas can be used to describe what variables a dataset is supposed to have,
    what types these variables take, and additional constraints on their values.
    When enforced, computations will return errors if the input dataset does not
    comply to the schema. To set a schema in a project, use `Project.set_input_schema`.

    This class offers high-level methods to build a schema.

    """

    model: models.DatasetSchema
    """
    API model for the schema
    """
    cols: Dict[str, models.ColumnSchema]
    """
    Dictionary from column names to column schema
    """

    def __init__(self, model: models.DatasetSchema = None):
        """
        Creates a dataset schema.

        Args:
            model (models.DatasetSchema, optional): an API model representing a dataset schema to
                initialize this object. Defaults to None.
        """
        self.model = model
        if model is None:
            self.model = models.DatasetSchema(columns=models.DatasetSchemaColumns())
            self.model.columns.additional_properties = {}
        self.cols = self.model.columns.additional_properties

    @classmethod
    def infer_from_datasource(
        cls,
        ds: "DataSource",
        dp_epsilon: float = None,
        query: models.DataSourceQuery = None,
    ):
        """
        Infers the dataset schema of a datasource.

        The inference occurs in the Tune Insight instance: no data is transferred outside of the
        security perimeter. If the data is highly sensitive, this inference process can be required
        to use differential privacy. The resulting schema will be less accurate (i.e., minimum and
        maximum bounds will be loose) but will not reveal information about any single record.

        Note that this schema can contain mistakes: it is recommended to carefully vet the resulting
        object before it is used for data-critical tasks.

        Args:
            ds (DataSource): the input datasource
            dp_epsilon (float, optional): if specified, this inference process uses differential privacy.
                Defaults to None.
            query (models.DataSourceQuery, optional): a query to extract data from the datasource.

        """
        if query is None:
            query = ds.local_query_parameters
        res = post_data_source_infer_schema.sync_detailed(
            ds.get_id(),
            client=ds.client,
            dp_epsilon=dp_epsilon,
            json_body=query,
        )
        validate_response(res)
        return cls(res.parsed)

    def set_drop_invalid(self, drop: bool = True):
        """Sets whether rows that do not match the schema should be dropped."""
        self.model.drop_invalid_rows = drop

    def add_column(
        self,
        name: str,
        dtype: str = None,
        coerce: bool = False,
        nullable: bool = False,
        required: bool = True,
    ) -> models.ColumnSchema:
        """
        Creates a new column and adds it to the dataset schema.

        Args:
            name (str): the name of the column.
            dtype (str, optional): the expected column data type. Defaults to None.
            coerce (bool, optional): whether errors should be coerced when validating. Defaults to False.
            nullable (bool, optional): whether the column is nullable. Defaults to False.
            required (bool, optional): whether the column is required. Defaults to True.

        Returns:
            ColumnSchema: the newly created column schema model
        """
        col = models.ColumnSchema(nullable=nullable, coerce=coerce, required=required)
        if dtype is not None:
            col.dtype = dtype
        col.checks = models.ColumnSchemaChecks()
        self.cols[name] = col
        return col

    def get_column(self, name: str) -> models.ColumnSchema:
        """
        Returns the corresponding column schema for the column identified by 'name'.

        Args:
            name (str): the name of the column.

        Returns:
            models.ColumnSchema: the corresponding column schema
        """
        if name not in self.cols:
            return self.add_column(name=name)
        return self.cols[name]

    def lt(self, name: str, val: Any):
        """
        Adds a requirement that checks that values from the column are less than `val`.

        Args:
            name (str): the column name.
            val (Any): the upper bound value.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.lt = val
        return self

    def le(self, name: str, val: Any):
        """
        Adds a requirement that checks that values from the column are less than or equal to `val`.

        Args:
            name (str): the column name.
            val (Any): the upper bound value.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.le = val
        return self

    def eq(self, name: str, val: Any):
        """
        Adds a requirement that checks that values from the column are equal to `val`.

        Args:
            name (str): the column name.
            val (Any): the value to compare with.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.eq = val
        return self

    def ge(self, name: str, val: Any):
        """
        Adds a requirement that checks that values from the column are greater or equal to `val`.

        Args:
            name (str): the column name.
            val (Any): the lower bound value.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.ge = val
        return self

    def gt(self, name: str, val: Any):
        """
        Adds a requirement that checks that values from the column are greater than `val`.

        Args:
            name (str): the column name.
            val (Any): the lower bound value.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.gt = val
        return self

    def in_range(
        self,
        name: str,
        min_value: float,
        max_value: float,
        include_min: bool = True,
        include_max: bool = True,
    ):
        """
        Adds a requirement that checks that values from the column all belong to a specified range.

        Args:
            name (str): name of the column.
            min_value (float): minimum value in the range.
            max_value (float): maximum value in the range.
            include_min (bool, optional): whether the minimum value is include in the range. Defaults to True.
            include_max (bool, optional): whether the maximum value is included in the range. Defaults to True.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.in_range = models.ColumnSchemaChecksInRange(
            max_value=max_value,
            min_value=min_value,
            include_min=include_min,
            include_max=include_max,
        )
        return self

    def str_startswith(self, name: str, val: str):
        """
        Adds a requirement that checks that all values from the column start with a specific substring.

        Args:
            name (str): the name of the column
            val (str): the substring
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.str_startswith = val
        return self

    def isin(self, name: str, vals: List[Any]):
        """
        Adds a requirement that checks that all values from the column are from a specified set of values.

        Args:
            name (str): the name of the column.
            vals (List[Any]): the specified set of values.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.isin = vals
        return self

    def notin(self, name: str, vals: List[Any]):
        """
        Adds a requirement that checks that all values from the column are excluded from specified set of values.

        Args:
            name (str): the name of the column
            vals (List[Any]): the set of values to exclude
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.checks.isin = vals
        return self

    def required(self, name: str, required: bool):
        """
        Sets whether a column is required (default) or optional.

        Args:
            name (str): the name of the column.
            required (bool): whether the column is required.
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.required = required
        return self

    def dtype(self, name: str, dtype: str):
        """
        Sets the data type to require for a column.

        Args:
            name (str): the name of the column
            dtype (str): the required data type
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.dtype = dtype
        return self

    def nullable(self, name: str, nullable: bool):
        """
        Sets whether a column is nullable (True by default).

        Args:
            name (str): the name of the column
            nullable (bool): whether the column is nullable
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.nullable = nullable
        return self

    def coerce(self, name: str, coerce: bool):
        """
        Sets the coerce value of the column.

        Args:
            name (str): the name of the column
            coerce (bool): whether the validator should coerce invalid types
        Returns:
            self (DatasetSchema): the updated schema
        """
        col = self.get_column(name)
        col.coerce = coerce
        return self

    def display(self):
        """Renders this dataset schema in a human-readable format."""
        display_dataset_schema(self)

    @property
    def name(self) -> str:
        """Name of this schema, if any."""
        return self.model.name


_dtype_names = {
    "str": "Categorical or freeform data (including identifiers)",
    "int": "Integer-valued data",
    "float": "Continuous-valued data",
    "datetime": "Dates and/or times",
    UNSET: "Unknown",
}


def display_dataset_schema(schema: DatasetSchema):
    r = Renderer()
    if is_set(schema.name):
        r.h1(schema.name)
    alphabetical_columns = sorted(schema.cols.keys())
    for column_name in alphabetical_columns:
        column_schema = schema.get_column(column_name)
        r.h2(column_schema.title)
        if is_set(column_schema.description):
            r.text(column_schema.description)
        r.text(r.bf("type:"), _dtype_names[column_schema.dtype], ".")
        required = value_if_unset(column_schema.required, False)
        r.text(f"This field is {'not ' if not required else ''}required.")

        if is_set(column_schema.checks):
            r.h3("Constraints")
            checks = column_schema.checks
            for value, op_text in [
                (checks.eq, "=="),
                (checks.ge, ">="),
                (checks.gt, ">"),
                (checks.isin, "is in"),
                (checks.le, "<="),
                (checks.lt, "<"),
                (checks.notin, "is not in"),
            ]:
                if is_set(value):
                    r.item(column_name, op_text, value)
            if is_set(checks.in_range):
                min_ = value_if_unset(checks.in_range.min_value, 0)
                max_ = value_if_unset(checks.in_range.max_value, 0)
                if column_schema.dtype == "int":
                    min_, max_ = int(min_), int(max_)
                    if max_ - min_ < 8:
                        r.item(
                            f"{column_name} is in {{{', '.join(str(x) for x in range(min_, max_ + 1))}}}",
                        )
                    else:
                        r.item(
                            f"{column_name} is in {{{min_}, {min_+1}, ..., {max_-1}, {max_}}}"
                        )
                else:
                    r.item(f"{column_name} is in the range [{min_}, {max_}]")
