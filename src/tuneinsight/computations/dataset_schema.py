from typing import Dict,List,Any
from tuneinsight.api.sdk import models


class DatasetSchema:
    '''
    DatasetSchema represents a user-defined dataset schema that inputs must comply to
    '''

    model: models.DatasetSchema
    '''
    API model for the schema
    '''
    cols: Dict[str,models.ColumnSchema]
    '''
    Dictionary from column names to column schema
    '''



    def __init__(self):
        self.cols = {}
        self.model = models.DatasetSchema(columns=models.DatasetSchemaColumns())
        self.model.columns.additional_properties = self.cols


    def drop_invalid(self,drop: bool = True):
        self.model.drop_invalid_rows = drop

    def add_column(self,name:str,dtype: str = None,
                   coerce: bool = False,
                   nullable: bool = False,
                   required: bool = True) -> models.ColumnSchema:
        '''
        add_column creates a new column and adds it to the dataset schema

        Args:
            name (str): the name of the column
            dtype (str, optional): the expected column data type. Defaults to None.
            coerce (bool, optional): whether errors should be coerced when validating. Defaults to False.
            nullable (bool, optional): whether the column is nullable. Defaults to False.
            required (bool, optional): whether the column is required. Defaults to True.

        Returns:
            ColumnSchema: the newly created column schema model
        '''
        col = models.ColumnSchema(nullable=nullable,coerce=coerce,required=required)
        if dtype is not None:
            col.dtype = dtype
        col.checks = models.ColumnSchemaChecks()
        self.cols[name] = col
        return col

    def get_column(self,name:str) -> models.ColumnSchema:
        '''
        get_column returns the corresponding column schema

        Args:
            name (str): the name of the column

        Returns:
            models.ColumnSchema: the corresponding column schema
        '''
        if name not in self.cols:
            return self.add_column(name=name)
        return self.cols[name]

    def lt(self,name:str,val: Any):
        '''
        lt requires values from the column to be less than 'val'

        Args:
            name (str): the column name
            val (Any): the upper bound value
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.lt = val
        return self

    def le(self,name:str,val: Any):
        '''
        le requires values from the column to be less than or equal to 'val'

        Args:
            name (str): the column name
            val (Any): the upper bound value
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.le = val
        return self

    def eq(self,name:str,val: Any):
        '''
        eq requires values from the column to be equal to 'val'

        Args:
            name (str): the column name
            val (Any): the value to compare with
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.eq = val
        return self

    def ge(self,name:str,val: Any):
        '''
        ge requires values from the column to be greater or equal to 'val'

        Args:
            name (str): the column name
            val (Any): the lower bound value
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.ge = val
        return self

    def gt(self,name:str,val: Any):
        '''
        gt requires values from the column to be greater than 'val'

        Args:
            name (str): the column name
            val (Any): the lower bound value
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.gt = val
        return self

    def in_range(self,name:str,min_value: float,max_value: float,include_min: bool = True,include_max: bool = True):
        '''
        in_range requires values from the column to be in a specified range

        Args:
            name (str): name of the column
            min_value (float): minimum value in the range
            max_value (float): maximum value in the range
            include_min (bool, optional): whether the minimum value is include in the range. Defaults to True.
            include_max (bool, optional): whether the maximum value is included in the range. Defaults to True.
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.in_range = models.ColumnSchemaChecksInRange(max_value=max_value,min_value=min_value,include_min=include_min,include_max=include_max)
        return self

    def str_startswith(self,name:str,val:str):
        '''
        str_startswith requires that all values from the column start with a specific substring

        Args:
            name (str): the name of the column
            val (str): the substring
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.str_startswith = val
        return self


    def isin(self,name:str,vals: List[Any]):
        '''
        isin requires that all values from the column are from a specified set of values

        Args:
            name (str): the name of the column
            vals (List[Any]): the specified set of values
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.isin = vals
        return self

    def notin(self,name:str,vals: List[Any]):
        '''
        notin requires that all values from the column are excluded from specified set of values

        Args:
            name (str): the name of the column
            vals (List[Any]): the set of values to exclude
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.checks.isin = vals
        return self

    def required(self,name:str,required: bool):
        '''
        required sets a column as required or optional

        Args:
            name (str): the name of the column
            required (bool): whether the column is required
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.required = required
        return self

    def dtype(self,name:str, dtype: str):
        '''
        dtype sets the required data type of the column

        Args:
            name (str): the name of the column
            dtype (str): the required data type
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.dtype = dtype
        return self

    def nullable(self,name:str, nullable: bool):
        '''
        dtype sets the nullable status of the column

        Args:
            name (str): the name of the column
            nullable (bool): whether the column is nullable
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.nullable = nullable
        return self

    def coerce(self,name:str, coerce: bool):
        '''
        dtype sets the coerce value of the column

        Args:
            name (str): the name of the column
            coerce (bool): whether the validator should coerce invalid types
        Returns:
            self (DatasetSchema): the updated schema
        '''
        col = self.get_column(name)
        col.coerce = coerce
        return self
