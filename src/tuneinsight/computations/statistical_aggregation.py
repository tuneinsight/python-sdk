from typing import Callable, Dict,List, Tuple, Union
import pandas as pd

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models import float_matrix
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.client.computations import ComputationRunner

class Aggregation(ComputationRunner):

    float_precision: int = 2
    target_column: str = ""
    join_id: str = ""
    values: List[str] = None
    aggregated_columns: List[str] = []
    count_columns: Dict[str,List[str]] = {}
    interval:List[float] = None

    @staticmethod
    def new_model() -> models.StatisticalAggregation:
        return models.StatisticalAggregation(type=models.ComputationType.STATISTICALAGGREGATION)


    def interval_to_categorical_label(self,interval) -> Callable[[str],str]:
        def res(cat: str) -> str:
            return self.interval_str(int(cat),interval)
        return res

    @staticmethod
    def value_to_categorical_label() -> Callable[[str],str]:
        def res(cat:str) -> str:
            return cat
        return res

    def run(self,comp: models.StatisticalAggregation,local: bool) -> models.FloatMatrix:
        dataobjects = super().run_computation(comp=comp,local=local,release=True)
        return dataobjects[0].get_float_matrix()

    @staticmethod
    def interval_str(interval_index: int,interval: List[float]) -> str:
        res = "-"
        if interval_index < len(interval):
            res = res + str(interval[interval_index])
        if interval_index > 0:
            res = str(interval[interval_index -1]) + res
        return res

    @staticmethod
    def parse_aggregation(result: float_matrix) -> Dict:
        vals = result.data[0]
        totals = {}
        for i,col_info in enumerate(result.contextual_info.columns_info):
            if col_info.value_type == models.ColumnInfoValueType.ROWCOUNT:
                totals["row_count"] = vals[i]
            else:
                totals[col_info.origin_column] = vals[i]

        return totals

    def count(self, local: bool = False) -> Union[int,pd.DataFrame]:
        """count returns the number of records

        Args:
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            Union[int,pd.DataFrame]: the number of records as an int or as a dataframe if a group by was set beforehand
        """

        columns_to_extract = []
        if len(self.count_columns) > 0:
            extracted_dict = [vals + ['other ' + k] for k,vals in self.count_columns.items()]
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

        model = self.new_model()
        model.include_dataset_length = True
        result = self.run(comp=model,local=local)

        parsed = self.parse_aggregation(result)

        return round(parsed["row_count"])

    def sum(self, columns: List[str], local: bool = False) -> pd.DataFrame:
        """sum returns the total for each given column

        Args:
            columns (List[str]): columns to compute sum on
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            pd.DataFrame: the sum for each column
        """
        if self.values is not None:
            self.aggregated_columns = columns # pylint: disable=W0201
            result = self.group_by_value(local=local)
            columns_to_extract = [self.target_column] + ["total " + col for col in columns]
            return result[columns_to_extract]
        if self.interval is not None:
            self.aggregated_columns = columns # pylint: disable=W0201
            result = self.group_by_interval(local=local)
            columns_to_extract = [self.target_column] + ["total " + col for col in columns]
            return result[columns_to_extract]

        model = self.new_model()
        model.aggregation_columns = columns

        result = self.run(comp=model,local=local)

        parsed = self.parse_aggregation(result)

        return pd.DataFrame.from_dict(parsed, orient='index', columns=["Total"])

    def average(self, columns: List[str], local: bool = False) -> pd.DataFrame:
        """average returns the average value for each given column

        Args:
            columns (List[str]): columns to compute average on
            local (bool, optional): whether to perform the operation only on local data or collectively. Defaults to False.

        Returns:
            pd.DataFrame: the average for each column
        """

        if self.values is not None:
            self.aggregated_columns = columns # pylint: disable=W0201
            result = self.group_by_value(local=local)
            columns_to_extract = [self.target_column] + ["average " + col for col in columns]
            return result[columns_to_extract]
        if self.interval is not None:
            self.aggregated_columns = columns # pylint: disable=W0201
            result = self.group_by_interval(local=local)
            columns_to_extract = [self.target_column] + ["average " + col for col in columns]
            return result[columns_to_extract]

        model = self.new_model()
        model.aggregation_columns = columns
        model.include_dataset_length = True

        result = self.run(comp=model,local=local)
        parsed = self.parse_aggregation(result)

        dataset_length = round(parsed["row_count"])
        parsed.pop("row_count")
        cols = []
        data = []
        for column_name,total in parsed.items():
            cols.append("average " + column_name)
            if dataset_length != 0:
                data.append(round(total/float(dataset_length),self.float_precision))
            else:
                data.append(0)
        return pd.DataFrame(data=[data],columns=cols)


    def group_by(self, target_col:str = None, values: List[str] = None, interval: List[float] = None, count_columns: Dict[str,List[str]] = {}): # pylint: disable=W0102
        """group_by sets attributes to perform grouped aggregations

        Args:
            target_col (str, optional): name of the column on which to perform the group by operation
            values (List[str], optional): values of the column on which to group
            interval (List[float], optional): intervals on which to group
            count_columns (Dict[str,List[str]], optional): values on which to compute a count percentage
        """

        self.target_column = target_col
        self.values = values
        self.interval = interval
        self.count_columns = count_columns


    def group_by_to_dataframe(self,cat_labels: List[str],counts: Dict[str,int],totals: Dict[str,float]) -> pd.DataFrame:
        # Create the data frame columns
        cols = [self.target_column,"count"]
        # categorical data
        for col,vals in self.count_columns.items():
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
            tmp = [cat,count]

            # fetch the categorical counts
            for col,vals in self.count_columns.items():
                for v in vals:
                    if count != 0:
                        tmp.append(round(counts[cat + col + v] / count * 100,self.float_precision))
                    else:
                        tmp.append(0)
                tmp.append(round(counts[cat + col + "other"] / count * 100,self.float_precision))
            # fetch the numerical aggregations
            for col in self.aggregated_columns:
                tot = totals[cat + col]
                tmp.append(round(tot,self.float_precision))
                if count != 0:
                    tmp.append(round(tot / float(count),self.float_precision))
                else:
                    tmp.append(0)
            data.append(tmp)

        return pd.DataFrame(data=data,columns=cols)

    @staticmethod
    def process_group_by_columns(column_infos: List[models.ColumnInfo],
                                 vals: List[float],cat_to_label: Callable[[str],str]) -> Tuple[Dict[str,int],Dict[str,float],List[str]]:
        counts = {}
        totals = {}
        categories = {}
        for i,col_info in enumerate(column_infos):
            cat_label = cat_to_label(col_info.group_info.category)
            categories[cat_label] = True
            if col_info.value_type == models.ColumnInfoValueType.ROWCOUNT:
                if col_info.origin_column == UNSET:
                    counts[cat_label] = int(vals[i])
                else:
                    counts[cat_label + col_info.origin_column + col_info.origin_value] = int(vals[i])
            else:
                totals[cat_label + col_info.origin_column] = vals[i]
        return counts,totals,categories.keys()



    def group_by_value(self,local: bool = False) -> pd.DataFrame:
        # create groupBy Value model
        model = self.new_model()
        cc :List[models.CategoricalColumn] = []
        for col,vals in self.count_columns.items():
            cc.append(models.CategoricalColumn(name=col,values=vals))
        bin_operation: models.BinningOperation = models.BinningOperation(aggregated_columns=self.aggregated_columns,
                                                                     categories=self.values,
                                                                     group_by_type=models.GroupByType.CATEGORY,
                                                                     target_column=self.target_column,
                                                                     count_columns=cc)
        model.binning_operations = [bin_operation]

        # Run the computation
        result = self.run(comp=model,local=local)
        vals = result.data[0]

        # Process results
        counts,totals,categories = self.process_group_by_columns(result.contextual_info.columns_info,result.data[0],self.value_to_categorical_label())
        return self.group_by_to_dataframe(cat_labels=categories,counts=counts,totals=totals)


    def group_by_interval(self,local: bool = False) -> pd.DataFrame:

        model = self.new_model()
        cc :List[models.CategoricalColumn] = []
        for col,vals in self.count_columns.items():
            cc.append(models.CategoricalColumn(name=col,values=vals))
        bin_operation: models.BinningOperation = models.BinningOperation(aggregated_columns=self.aggregated_columns,
                                                                     range_values=self.interval,
                                                                     group_by_type=models.GroupByType.RANGE,
                                                                     target_column=self.target_column,
                                                                     count_columns=cc)
        model.binning_operations = [bin_operation]

        result = self.run(comp=model,local=local)
        vals = result.data[0]

        counts,totals,categories = self.process_group_by_columns(result.contextual_info.columns_info,result.data[0],self.interval_to_categorical_label(self.interval))
        return self.group_by_to_dataframe(cat_labels=categories,counts=counts,totals=totals)
