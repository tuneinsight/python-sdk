import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import  Response
from tuneinsight.api.sdk.api.api_private_search import get_private_search_database
from tuneinsight.client.session import PIRSession
from tuneinsight.client.project import Project
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.client.validation import validate_response
from tuneinsight.utils.plots import style_plot


class PrivateSearch(ComputationRunner):
    """ Private Search computation

    """

    pir_db: models.PrivateSearchDatabase
    pir_dataset_id: str = ''
    session: PIRSession

    def __init__(self,project: Project, pir_dataset: str):
        """
        __init__ initializes the private search computation and the corresponding session

        Args:
            project (Project): project to initialize the private search computation from
            pir_dataset (str): id of the private search dataset

        """
        super().__init__(client=project.client, project_id=project.get_id())
        self.pir_dataset_id = pir_dataset
        self.pir_db = self.get_pir_db()

        self.session = PIRSession(self.client, self.pir_db)
        self.session.upload_eval_keys()


    def query(self, query: str) -> pd.DataFrame:
        """Perform a private search query

        Args:
            query (str): search query

        Returns:
            pd.DataFrame: private search result
        """
        pir = models.PrivateSearch(type=models.ComputationType.PRIVATESEARCH)
        pir.pir_dataset_object_id = self.pir_dataset_id
        try:
            pir.pir_search_object_id = self.session.encrypt_query(query)
        except ValueError:
            return pd.DataFrame()
        dataobjects = super().run_computation(comp=pir,keyswitch=False,decrypt=False)
        result = dataobjects[0].get_raw_data()
        return self.session.decrypt_response(result)

    @staticmethod
    def filter_result(result: pd.DataFrame, start: str = None, end: str = None, granularity: str = None) -> pd.DataFrame:
        """Filter the query result on dates

        Args:
            result (pd.DataFrame): query result
            start (str, optional): start date. Defaults to None.
            end (str, optional): end date. Defaults to None.
            granularity (str, optional): rule on which to resample results (e.g. 'W-Mon' resamples results on a week granularity where weeks begin on a Monday). Defaults to None.

        Returns:
            pd.DataFrame: filtered result
        """
        filtered_result = result.transpose(copy=True)
        if start is not None:
            filtered_result = filtered_result.loc[start:]
        if end is not None:
            filtered_result = filtered_result.loc[:end]
        if granularity is not None:
            filtered_result = filtered_result.reset_index()
            filtered_result['Date'] = pd.to_datetime(filtered_result['index'])
            filtered_result = filtered_result.resample(granularity, on='Date').sum()
        return filtered_result.transpose()

    @staticmethod
    def plot_result(result: pd.DataFrame, title:str,x_label:str, y_label:str, size:tuple=(8,4),timestamps: bool = False):
        """Plot the private search result

        Args:
            result (pd.DataFrame): private search result
            title (str): plot title
            x_label (str): plot x axis label
            y_label (str): plot y axis label
            size (tuple, optional): plot size. Defaults to (8,4).
            timestamps (bool, optional): whether or not the result columns are timestamps. Defaults to False.
        """
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        x_vals = result.columns
        if timestamps:
            x_vals = pd.to_datetime(x_vals)
        x = list(x_vals)
        y = [int(v) for v in list(result.iloc[0])]
        if timestamps:
            ax.plot(x, y, color="#DE5F5A", linewidth=2.5)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        else:
            ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)
        style_plot(ax, fig, title, x_label, y_label, size=size)

        plt.show()


    def get_pir_db(self) -> models.PrivateSearchDatabase:
        """Retrieve the private search database given the client and database id

        Returns:
            models.PrivateSearchDatabase: the private search database
        """
        self.client.timeout = 30
        response: Response[models.PrivateSearchDatabase] = get_private_search_database.sync_detailed(client=self.client,database_id=self.pir_dataset_id)
        validate_response(response)
        return response.parsed
