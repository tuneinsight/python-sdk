from typing import List, Any
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner


class SetIntersection(ComputationRunner):
    """
    SetIntersection Represents the private set intersection computation

    Args:
        ComputationRunner: Inherits all methods available from the computation runner parent class
    """

    def find_matches(
        self,
        col: str = None,
        value: Any = None,
        cols: List[str] = None,
        values: List[Any] = None,
        data: pd.DataFrame = None,
        fuzzy: bool = False,
        fuzzy_cols: bool = None,
    ) -> pd.DataFrame:
        """
        find_matches returns a dataframe that contains the result of the private set intersection across all nodes using the provided
        column list as the matching columns. If an input is provided here then the remote instance will use it as its own input instead of
        querying the database.

        Args:
            col (str, optional): the single column to match items on. Defaults to None.
            value (Any, optional): the single value to use as a local input. Defaults to None.
            cols (List[str], optional): the list of joint columns to match items on. Defaults to None.
            values (List[Any], optional):the list of values to use as local inputs. Defaults to None.
            data (pd.DataFrame, optional): the dataframe to use as a local input. Defaults to None.
            fuzzy (bool, optional): whether or not fuzzy matching is used. Defaults to False.
            fuzzy_cols (bool, optional): the list of columns that should be fuzzy matched. Defaults to None.

        Raises:
            ValueError: in case invalid arguments are passed.

        Returns:
            pd.DataFrame: the list of items that matched with other instances.
        """

        model = models.SetIntersection(type=models.ComputationType.SETINTERSECTION)
        if col is not None:
            cols = [col]
        if cols is None:
            raise ValueError("columns must be provided")
        model.matching_columns = [str(col) for col in cols]

        if value is not None:
            values = [value]
        if values is not None:
            data = pd.DataFrame(data=values, columns=cols)

        if data is not None:
            self.set_local_input(data)

        if fuzzy:
            if fuzzy_cols is None:
                fuzzy_cols = cols
            model.fuzzy_params = models.FuzzyMatchingParameters(
                phonetic_columns=model.matching_columns
            )

        results = self.run_computation(model, local=False, release=True)
        return results[0].get_dataframe()
