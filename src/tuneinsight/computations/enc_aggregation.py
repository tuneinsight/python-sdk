import pandas as pd
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.utils.plots import style_plot

class EncryptedAggregation(ComputationRunner):


    cohort_id: str = ""
    join_id: str = ""


    def get_model(self) -> models.EncryptedAggregation:
        model = models.EncryptedAggregation(type=models.ComputationType.ENCRYPTEDAGGREGATION)
        model.project_id = self.project_id
        model.cohort_id = self.cohort_id
        model.join_id = self.join_id
        return model


    def get_aggregation(self, local: bool = False) -> pd.DataFrame:

        model = self.get_model()
        dataobjects = super().run_computation(comp=model,local=local,keyswitch= not local,decrypt=True)
        result = dataobjects[0].get_float_matrix()
        totals = result.data[0]

        if len(result.columns) == len(totals):
            data = {'Column': result.columns, 'Total': totals}
        else:
            data = totals

        return pd.DataFrame(data)

    @staticmethod
    def plot_aggregation(result:pd.DataFrame, title:str, x_label:str, y_label:str, size:tuple=(8,4)):
        plt.style.use("bmh")
        fig, ax = plt.subplots()

        x = list(result.Column)
        y = list(result.Total)

        ax.bar(x, y, color="#DE5F5A", edgecolor="#354661", linewidth=2.5)

        style_plot(ax, fig, title, x_label, y_label, size=size)

        plt.show()



    def display_workflow(self):
        '''
        display_workflow displays the workflow of the encrypted aggregation
        '''
        return super().display_documentation(self.get_model())
