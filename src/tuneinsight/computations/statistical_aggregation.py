"""Aggregation computation that supports group-by operations."""

from typing import Callable, Dict, List, Tuple, Union
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models import float_matrix
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation


# TOFIX: this code is confusing to read and should be refactored. This will be part
# of the refactoring (https://github.com/tuneinsight/app/issues/1469).

# [Proposal]: group this with EncryptedAggregation. There are differences in the
#  backend, but the current state of affairs is very confusing for users (and me).
#  Even if the computations are different, it would make sense to group them.


def _interval_to_categorical_label(interval) -> Callable[[str], str]:
    """Closure that returns a labeller function for an interval."""
    return lambda cat: _interval_descriptor(int(cat), interval)


def _value_to_categorical_label() -> Callable[[str], str]:
    """Closure that returns a labeller function for categories."""
    return lambda cat: cat


def _interval_descriptor(interval_index: int, interval: List[float]) -> str:
    """Returns a string describing an interval from several."""
    res = "-"
    if interval_index < len(interval):
        res = res + str(interval[interval_index])
    if interval_index > 0:
        res = str(interval[interval_index - 1]) + res
    return res


def _parse_aggregation(result: float_matrix) -> Dict:
    """Parses the output of a computation to a dictionary."""
    vals = result.data[0]
    totals = {}
    for i, col_info in enumerate(result.contextual_info.columns_info):
        if col_info.value_type == models.ColumnInfoValueType.ROWCOUNT:
            totals["row_count"] = vals[i]
        else:
            totals[col_info.origin_column] = vals[i]
    return totals


def _sanitize_output(df: pd.DataFrame) -> pd.DataFrame:
    """Removes any invalid values (e.g. due to aggregation overflows) from the output dataset."""
    # Filters any rows that contain negative values (due to overflow)
    df = df[~df.select_dtypes(include="number").lt(0).any(axis=1)]
    return df


def _process_group_by_columns(
    column_infos: List[models.ColumnInfo],
    vals: List[float],
    cat_to_label: Callable[[str], str],
) -> Tuple[Dict[str, int], Dict[str, float], List[str]]:
    """Post-process the output of a groupby computation."""
    counts = {}
    totals = {}
    categories = {}
    for i, col_info in enumerate(column_infos):
        cat_label = cat_to_label(col_info.group_info.category)
        categories[cat_label] = True
        if col_info.value_type == models.ColumnInfoValueType.ROWCOUNT:
            if col_info.origin_column == UNSET:
                counts[cat_label] = int(vals[i])
            else:
                counts[cat_label + col_info.origin_column + col_info.origin_value] = (
                    int(vals[i])
                )
        else:
            totals[cat_label + col_info.origin_column] = vals[i]
    return counts, totals, categories.keys()


class GroupByAggregation(ModelBasedComputation):
    """
    An Aggregation Computation with groupby operations.

    This operation computes the aggregation (SUM) of all values in some columns,
    divided into several groups. These groups are defined either by intervals
    for continuous attributes, or values for categorical ones.

    Use the .groupby method to set the grouping parameters.

    Note: this computation will likely be deprecated soon, and grouped within the
    EncryptedAggregation computation.

    """

    # High-lever parameter on output smoothing.
    float_precision: int = 2
    # Internal parameters: the description of the groupby operation.
    target_column: str = ""
    values: List[str] = None
    interval: List[float] = None
    count_columns: Dict[str, List[str]] = {}
    # Other computation parameters.
    join_id: str = ""
    aggregated_columns: List[str] = []

    def __init__(self, project: "Project", keep_non_categorized_items: bool = True):
        """
        Creates an Aggregation computation.

        Args
            project (client.Project): the project to which this computation belongs.
            keep_non_categorized_items (bool, optional): whether non-binned leftover records
            should be included in the aggregation. Defaults to False.

        """
        super().__init__(
            project,
            models.StatisticalAggregation,
            models.ComputationType.STATISTICALAGGREGATION,
        )
        self._labeller = None
        self.keep_non_categorized_items = keep_non_categorized_items

    def _reset_model(self):
        """Reset the internal memory of the model."""
        self.model = models.StatisticalAggregation(
            type=models.ComputationType.STATISTICALAGGREGATION
        )

    def _process_results(self, dataobjects):
        """Apply parsing functions to the raw outputs."""
        # Apply generic parsing of the results.
        result = dataobjects[0].get_float_matrix()
        # The groupby methods sets a labeller. If None, assume the result is not from a groupby.
        if self._labeller is None:
            return _parse_aggregation(result)
        # Otherwise, parse the output groupby as a dataframe.
        counts, totals, categories = _process_group_by_columns(
            result.contextual_info.columns_info,
            result.data[0],
            self._labeller,
        )
        return self._group_by_to_dataframe(
            cat_labels=categories, counts=counts, totals=totals
        )

    ## Small utility function.

    def round_value(self, val: any) -> Union[int, float]:
        """
        Rounds a value to a small number of decimals.

        If the value is very close (<1e-5) to an integer, this returns the
        integer. Otherwise, this rounds to self.float_precision (default 2).

        """
        val = float(val)
        if abs(val - round(val)) < 0.00001:
            return int(val)
        return round(val, self.float_precision)

    ## High-level interfaces.

    def count(self, local: bool = False) -> Union[int, pd.DataFrame]:
        """
        Returns the number of records in the dataset.

        Args:
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            Union[int,pd.DataFrame]: the number of records as an int or as a dataframe if a group by was set beforehand
        """

        columns_to_extract = []
        if len(self.count_columns) > 0:
            extracted_dict = [
                vals + ["other " + k] for k, vals in self.count_columns.items()
            ]
            flattened = [v for sublist in extracted_dict for v in sublist]
            columns_to_extract.extend(flattened)
        if self.values is not None:
            result = self.group_by_value(local=local)
            columns_to_extract = [self.target_column, "count"] + columns_to_extract
            return result[columns_to_extract]
        if self.interval is not None:
            result = self.group_by_interval(local=local)
            columns_to_extract = [self.target_column, "count"] + columns_to_extract
            return result[columns_to_extract]

        self._reset_model()
        self.model.include_dataset_length = True
        result = self.run(local=local, release=True)

        return round(result["row_count"])

    def sum(self, columns: List[str], local: bool = False) -> pd.DataFrame:
        """
        Returns the sum of each selected column.

        Args:
            columns (List[str]): columns to compute sum on
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            pd.DataFrame: the sum for each column
        """
        if self.values is not None:
            self.aggregated_columns = columns  # pylint: disable=W0201
            result = self.group_by_value(local=local)
            columns_to_extract = [self.target_column] + [
                "total " + col for col in columns
            ]
            return result[columns_to_extract]
        if self.interval is not None:
            self.aggregated_columns = columns  # pylint: disable=W0201
            result = self.group_by_interval(local=local)
            columns_to_extract = [self.target_column] + [
                "total " + col for col in columns
            ]
            return result[columns_to_extract]

        self._reset_model()
        self.model.aggregation_columns = columns
        result = self.run(local=local, release=True)

        return pd.DataFrame.from_dict(result, orient="index", columns=["Total"])

    def average(self, columns: List[str], local: bool = False) -> pd.DataFrame:
        """Returns the average value for each selected column.

        Args:
            columns (List[str]): columns to compute average on
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            pd.DataFrame: the average for each column
        """

        if self.values is not None:
            self.aggregated_columns = columns  # pylint: disable=W0201
            result = self.group_by_value(local=local)
            columns_to_extract = [self.target_column] + [
                "average " + col for col in columns
            ]
            return result[columns_to_extract]
        if self.interval is not None:
            self.aggregated_columns = columns  # pylint: disable=W0201
            result = self.group_by_interval(local=local)
            columns_to_extract = [self.target_column] + [
                "average " + col for col in columns
            ]
            return result[columns_to_extract]

        self._reset_model()
        self.model.aggregation_columns = columns
        self.model.include_dataset_length = True

        result = self.run(local=local, release=True)

        dataset_length = round(result["row_count"])
        result.pop("row_count")
        cols = []
        data = []
        for column_name, total in result.items():
            cols.append("average " + column_name)
            if dataset_length != 0:
                data.append(self.round_value(total / float(dataset_length)))
            else:
                data.append(0)
        return pd.DataFrame(data=[data], columns=cols)

    def group_by(
        self,
        target_col: str = None,
        values: List[str] = None,
        interval: List[float] = None,
        count_columns: Dict[str, List[str]] = {},
    ):  # pylint: disable=W0102
        """
        Sets internal attributes to perform grouped aggregations.

        Args:
            target_col (str, optional): name of the column on which to perform the groupby operation
            values (List[str], optional): values of the column on which to group (for categorical attributes).
            interval (List[float], optional): intervals on which to group (for continuous attributes).
            count_columns (Dict[str,List[str]], optional): values on which to compute a count. TODO what is this?
        """
        if values is not None and interval is not None:
            raise ValueError("Cannot set both values and interval: choose one.")
        self.target_column = target_col
        self.values = values
        self.interval = interval
        self.count_columns = count_columns

    def _group_by_to_dataframe(
        self, cat_labels: List[str], counts: Dict[str, int], totals: Dict[str, float]
    ) -> pd.DataFrame:
        """Converts the output of a groupby operation to a DataFrame."""
        # Create the data frame columns.
        cols = [self.target_column, "count"]
        # categorical data
        for col, vals in self.count_columns.items():
            for v in vals:
                cols.append(v)
            cols.append("other " + col)
        # numerical data
        for col in self.aggregated_columns:
            cols.append("total " + col)
            cols.append("average " + col)

        # create the rows
        data = []
        # iterate over each category
        for cat in cat_labels:
            # add category + count
            count = counts[cat]
            tmp = [cat, count]

            # fetch the categorical counts
            for col, vals in self.count_columns.items():
                for v in vals:
                    if count != 0:
                        tmp.append(
                            self.round_value(
                                counts[cat + col + v] / count * 100,
                            )
                        )
                    else:
                        tmp.append(0)
                tmp.append(self.round_value(counts[cat + col + "other"] / count * 100))
            # fetch the numerical aggregations
            for col in self.aggregated_columns:
                tot = totals[cat + col]
                tmp.append(self.round_value(tot))
                if count != 0:
                    tmp.append(self.round_value(tot / float(count)))
                else:
                    tmp.append(0)
            data.append(tmp)
        result = pd.DataFrame(data=data, columns=cols)
        return _sanitize_output(result)

    def group_by_value(self, local: bool = False) -> pd.DataFrame:
        """Performs this operation, grouping by value."""
        # create groupBy Value model
        self._reset_model()
        cc = []
        for col, vals in self.count_columns.items():
            cc.append(models.CategoricalColumn(name=col, values=vals))
        bin_operation = models.BinningOperation(
            aggregated_columns=self.aggregated_columns,
            categories=self.values,
            group_by_type=models.GroupByType.CATEGORY,
            target_column=self.target_column,
            keep_non_categorized_items=self.keep_non_categorized_items,
            count_columns=cc,
        )
        self.model.binning_operations = [bin_operation]
        self._labeller = _value_to_categorical_label()
        # Run the computation.
        return self.run(local=local, release=True)

    def group_by_interval(self, local: bool = False) -> pd.DataFrame:
        """Performs this computation, grouping by interval."""
        self._reset_model()
        cc = []
        for col, vals in self.count_columns.items():
            cc.append(models.CategoricalColumn(name=col, values=vals))
        bin_operation = models.BinningOperation(
            aggregated_columns=self.aggregated_columns,
            range_values=self.interval,
            group_by_type=models.GroupByType.RANGE,
            target_column=self.target_column,
            keep_non_categorized_items=self.keep_non_categorized_items,
            count_columns=cc,
        )
        self.model.binning_operations = [bin_operation]
        self._labeller = _interval_to_categorical_label(self.interval)

        return self.run(local=local, release=True)
