from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.utils.plots import style_plot
from tuneinsight.client.dataobject import DataObject
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.computations.enc_aggregation import EncryptedAggregation
from tuneinsight.computations.gwas import GWAS


class Cohort(ComputationRunner):

    cohort_id: str = ""
    join_id: str = ""

    def create_from_matching(self, matching_columns: List[str], result_format: models.SetIntersectionOutputFormat, local_input: models.LocalInput = None) -> List[DataObject]:
        """ Create a cohort from matching columns

        Args:
            matching_columns (List[str]): a list of column names to match on
            result_format (models.SetIntersectionOutputFormat): the format to output the resulting cohort as
            local_input (models.LocalInput): optional local input to use in the computation

        Returns:
            List[DataObject]: The resulting dataobjects
        """
        model = models.SetIntersection(type=models.ComputationType.SETINTERSECTION)
        model.matching_columns = matching_columns
        model.result_format = result_format
        model.project_id = self.project_id

        if local_input:
            model.local_input = local_input

        dataobjects = super().run_computation(comp=model,local=False,release=True)
        self.cohort_id = dataobjects[0].get_id()
        return dataobjects

    @staticmethod
    def get_psi_ratio(all_parties: List[str], dataobjects: List[DataObject]) -> pd.DataFrame:
        """ Add a column to the PSI result indicating for each record the percentage of participants at which the record was observed

        Args:
            all_parties (List[str]): list of the names of the parties involved in the private set intersection
            dataobjects (List[DataObject]): psi result

        Returns:
            pd.DataFrame: parsed data
        """
        df = dataobjects[0].get_dataframe()
        num_parties = len(all_parties)
        percentages = []
        results = df.to_dict(orient='records')
        for row in results:
            match = 0
            for org in all_parties:
                if org in row and row[org] == 'true':
                    match += 1
            percentages.append(match/num_parties*100)
        df['psi_ratio'] = pd.Series(percentages)
        return df

    def create_from_join(self, target_columns: List[str], join_columns: List[str]):
        """ Create a cohort from vertically partitioned data

        Args:
            target_columns (List[str]): column names of target columns
            join_columns (List[str]): column names to join the data on
        """
        model = models.DistributedJoin(type=models.ComputationType.DISTRIBUTEDJOIN)
        model.target_columns = target_columns
        model.join_columns = join_columns
        model.project_id = self.project_id

        dataobjects = super().run_computation(comp=model,local=False,keyswitch=False,decrypt=False)

        self.join_id = dataobjects[0].get_id()


    def get_size(self,nodes: List[str]) -> pd.DataFrame:
        """ Get the size of each participants dataset in the cohort

        Args:
            nodes (List[str]): list of participant names to get the dataset size of

        Returns:
            pd.DataFrame: a dataframe containing the size of the resulting cohort dataset for each node
        """
        agg = self.new_aggregation()
        for n in nodes:
            agg.preprocessing.counts(output_column_name=n,nodes=[n])
            agg.preprocessing.select(columns=nodes,create_if_missing=True,dummy_value="0",nodes=[n])
        agg.preprocessing.select(columns=nodes,create_if_missing=True,dummy_value="0")
        return agg.get_aggregation()



    def new_aggregation(self) -> EncryptedAggregation:
        """ Create an aggregation computation on the cohort

        Raises:
            Exception: if the cohort hasn't been created beforehand

        Returns:
            EncryptedAggregation: the encrypted aggregation computation
        """
        if self.cohort_id == "" and self.join_id == "":
            raise Exception("cohort must be created before running an aggregation")

        aggregation = EncryptedAggregation(client=self.client, project_id=self.project_id)
        aggregation.cohort_id = self.cohort_id
        aggregation.join_id = self.join_id
        return aggregation

    def new_gwas(self) -> GWAS:
        """ Create an GWAS computation on the cohort

        Raises:
            Exception: if the cohort hasn't been created beforehand

        Returns:
            GWAS: the GWAS computation
        """
        if self.cohort_id == "" and self.join_id == "":
            raise Exception("cohort must be created before running a GWAS")

        gwas = GWAS(client=self.client, project_id=self.project_id)
        gwas.cohort_id = self.cohort_id
        gwas.join_id = self.join_id
        return gwas

    @staticmethod
    def plot_psi(x, y, title, x_label, y_label):
        """ Plot the PSI results as a bar graph

        Args:
            x (_type_): x values
            y (_type_): y values
            title (_type_): plot title
            x_label (_type_): plot x label
            y_label (_type_): plot y label
        """
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)
        style_plot(ax, fig, title, x_label, y_label)
        plt.show()
