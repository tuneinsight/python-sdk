from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.utils.plots import style_plot


class GWAS(ComputationRunner):
    """ Computation for a Genome-Wide Association Study (GWAS).

    Args:
        ComputationRunner (ComputationRunner): parent class for running computation through the REST API.
    """


    cohort_id: str = UNSET
    join_id: str = UNSET

    def linear_regression(self, target_label:str = UNSET, variants_organization:str = UNSET, matching_params:models.MatchingParams = UNSET, covariates:List[str] = UNSET, locus_range:models.LocusRange = UNSET, local: bool = False) -> pd.DataFrame:
        """ Run a linear regression for the GWAS.

        Args:
            target_label (str, optional): name of the column containing the phenotypical trait to study. Defaults to UNSET.
            variants_organization (str, optional): name of the nodes containing data on variants. Defaults to UNSET.
            matching_params (models.MatchingParams, optional): parameters to match the patients across the genomic and clinical data. Defaults to UNSET.
            covariates (List[str], optional): list of column names containing the covariates. Defaults to UNSET.
            locus_range (models.LocusRange, optional): locus range to analyse. Defaults to UNSET.
            local (bool, optional): whether to perform the computation locally. Defaults to False.

        Returns:
            pd.DataFrame: resulting p-values
        """
        model = models.GWAS(type=models.ComputationType.GWAS)
        model.project_id = self.project_id
        model.covariates = covariates
        model.locus_range = locus_range
        model.target_label = target_label
        model.variants_organization = variants_organization
        model.matching_params = matching_params
        model.cohort_id = self.cohort_id
        model.join_id = self.join_id
        model.timeout = 500
        # self.max_timeout = 5 * self.max_timeout

        dataobjects = super().run_computation(comp=model,local=local,keyswitch= not local,decrypt=True)
        result = dataobjects[0].get_float_matrix()
        p_values = result.data[0]

        if len(result.columns) == len(p_values):
            data = {'locus': result.columns, 'p_value': p_values}
        else:
            data = p_values

        return pd.DataFrame(data)

    def plot_manhattan(self, p_values: pd.DataFrame):
        """ Display the GWAS result as a manhattan plot.

        Args:
            p_values (pd.DataFrame): DataFrame containing p-values.
        """

        # Transform data for plot
        p_values = p_values[['locus', 'p_value']]
        p_values['chromosome'] = p_values[['locus']].applymap(lambda x: x.split(':')[0])
        p_values['minuslog10pvalue'] = -np.log10(p_values.p_value)
        p_values.chromosome = p_values.chromosome.astype('category')
        p_values['ind'] = range(len(p_values))
        p_grouped = p_values.groupby(('chromosome'))


        plt.style.use("bmh")

        fig, ax = plt.subplots()


        colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00', '#CC79A7', '#56B4E9', '#009E73','#F0E442']
        x_labels = []
        x_labels_pos = []
        for num, (name, group) in enumerate(p_grouped):
            group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], ax=ax)
            x_labels.append(name)
            x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
        ax.set_xticks(x_labels_pos)
        ax.set_xticklabels(x_labels)

        ax.set_xlim([0, len(p_values)])

        style_plot(axis=ax, fig=fig, title="Manhattan Plot for GWAS", x_label='Chromosome', y_label="P-value (-log10 scale)")

        plt.show()
