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

    def create_from_matching(self, matching_columns: List[str], result_format: models.SetIntersectionOutputFormat) -> List[DataObject]:
        model = models.SetIntersection(type=models.ComputationType.SETINTERSECTION)
        model.matching_columns = matching_columns
        model.result_format = result_format
        model.project_id = self.project_id
        dataobjects = super().run_computation(comp=model,local=False,keyswitch=False,decrypt=False)
        self.cohort_id = dataobjects[0].get_id()
        return dataobjects

    def parse_suricata_psi_output(self, all_parties: List[str], dataobjects: List[DataObject]) -> pd.DataFrame:
        df = dataobjects[0].get_dataframe()
        num_parties = len(all_parties)-1
        alert_ids  = df['alert_id']
        severities = df['alert_severity']
        categories = df['alert_category']
        percentages = []
        results = df.to_dict(orient='records')
        for row in results:
            match = 0
            for org in all_parties:
                if org in row and row[org] == 'true':
                    match += 1
            percentages.append(match/num_parties*100)
        data = {'alert_id': alert_ids, 'severity': severities, 'category': categories, 'customer_ratio': percentages}
        return pd.DataFrame(data)

    def create_from_join(self, target_columns: List[str], join_columns: List[str]):

        model = models.DistributedJoin(type=models.ComputationType.DISTRIBUTEDJOIN)
        model.target_columns = target_columns
        model.join_columns = join_columns
        model.project_id = self.project_id

        dataobjects = super().run_computation(comp=model,local=False,keyswitch=False,decrypt=False)

        self.join_id = dataobjects[0].get_id()


    def get_size(self,nodes: List[str]) -> pd.DataFrame:
        agg = self.new_aggregation()
        for n in nodes:
            agg.preprocessing.counts(output_column_name=n,nodes=[n])
            agg.preprocessing.select(columns=nodes,create_if_missing=True,dummy_value="0",nodes=[n])
        agg.preprocessing.select(columns=nodes,create_if_missing=True,dummy_value="0")
        return agg.get_aggregation()



    def new_aggregation(self) -> EncryptedAggregation:
        if self.cohort_id == "" and self.join_id == "":
            raise Exception("cohort must be created before running an aggregation")

        aggregation = EncryptedAggregation(client=self.client, project_id=self.project_id)
        aggregation.cohort_id = self.cohort_id
        aggregation.join_id = self.join_id
        return aggregation

    def new_gwas(self) -> GWAS:
        if self.cohort_id == "" and self.join_id == "":
            raise Exception("cohort must be created before running a GWAS")

        gwas = GWAS(client=self.client, project_id=self.project_id)
        gwas.cohort_id = self.cohort_id
        gwas.join_id = self.join_id
        return gwas


    def plot_psi(self, x, y, title, x_label, y_label):
        plt.style.use("bmh")
        fig, ax = plt.subplots()
        ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)
        style_plot(ax, fig, title, x_label, y_label)
        plt.show()
