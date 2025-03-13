"""Classes for Genome-Wide Association Studies (GWAS)."""

from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation, ComputationResult
from tuneinsight.utils.plots import style_plot

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET


class GWASResults(ComputationResult):
    """Results from a GWAS computation."""

    def __init__(self, result: DataContent):
        result = result.get_float_matrix()
        p_values = result.data[0]
        if len(result.columns) == len(p_values):
            data = {"locus": result.columns, "p_value": p_values}
        else:
            data = p_values
        self.result = pd.DataFrame(data)

    def as_table(self) -> pd.DataFrame:
        return self.result

    def plot(self):
        """Displays the GWAS result as a TI-branded manhattan plot."""
        # Transform data for plot
        p_values = self.result[["locus", "p_value"]]
        p_values["chromosome"] = p_values[["locus"]].map(lambda x: x.split(":")[0])
        p_values["minuslog10pvalue"] = -np.log10(p_values.p_value)
        p_values.chromosome = p_values.chromosome.astype("category")
        p_values["ind"] = range(len(p_values))
        p_grouped = p_values.groupby(("chromosome"))

        plt.style.use("bmh")
        fig, ax = plt.subplots()

        colors = [
            "#348ABD",
            "#A60628",
            "#7A68A6",
            "#467821",
            "#D55E00",
            "#CC79A7",
            "#56B4E9",
            "#009E73",
            "#F0E442",
        ]
        x_labels = []
        x_labels_pos = []
        for num, (name, group) in enumerate(p_grouped):
            group.plot(
                kind="scatter",
                x="ind",
                y="minuslog10pvalue",
                color=colors[num % len(colors)],
                ax=ax,
            )
            x_labels.append(name)
            x_labels_pos.append(
                (
                    group["ind"].iloc[-1]
                    - (group["ind"].iloc[-1] - group["ind"].iloc[0]) / 2
                )
            )
        ax.set_xticks(x_labels_pos)
        ax.set_xticklabels(x_labels)
        ax.set_xlim([0, len(p_values)])

        style_plot(
            axis=ax,
            fig=fig,
            title="Manhattan Plot for GWAS",
            x_label="Chromosome",
            y_label="p-value (-log10 scale)",
        )

        plt.show()


class GWAS(ModelBasedComputation):
    """
    Computation for a Genome-Wide Association Study (GWAS).

    Computes a linear regression over locuses in a GWAS, where different instances
    can hold different parts of the data (vertically partitioned data), and
    returns the p-values of the regression for each locus.

    """

    def __init__(
        self,
        project: "Project",
        target_label: str = UNSET,
        variants_organization: str = UNSET,
        matching_params: models.MatchingParams = UNSET,
        covariates: List[str] = UNSET,
        locus_range: models.LocusRange = UNSET,
        cohort: "Cohort" = None,
    ):
        """
        Creates a GWAS computation.

        Args
            project (client.Project): the project to which this computation belongs.
            target_label (str, optional): name of the column containing the phenotypical trait to study.
            variants_organization (str, optional): name of the nodes containing data on variants.
            matching_params (models.MatchingParams, optional): parameters to match the patients across
                the genomic and clinical data.
            covariates (List[str], optional): list of column names containing the covariates.
            locus_range (models.LocusRange, optional): range specification for locus genomic positions.
            cohort (Cohort, default None): if specified, the cohort of records over which this aggregation is computed.

        """
        super().__init__(
            project,
            models.GWAS,
            type=models.ComputationType.GWAS,
            target_label=target_label,
            variants_organization=variants_organization,
            matching_params=matching_params,
            covariates=covariates,
            locus_range=locus_range,
        )
        if cohort is not None:
            self.model.cohort_id = cohort.cohort_id
            self.model.join_id = cohort.join_id

    @classmethod
    def from_model(cls, project: "Project", model: models.GWAS) -> "GWAS":
        model = models.GWAS.from_dict(model.to_dict())
        with project.disable_patch():
            comp = GWAS(
                project,
                target_label=model.target_label,
                variants_organization=model.variants_organization,
                matching_params=model.matching_params,
                covariates=model.covariates,
                locus_range=model.locus_range,
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        """Returns the p-values of the GWAS linear regression."""
        return GWASResults(results[0])
