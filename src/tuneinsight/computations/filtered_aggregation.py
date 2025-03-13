"""Classes to implement the filtered aggregation computation."""

from typing import List

import pandas as pd

from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, false_if_unset


class FilteredAggregation(ModelBasedComputation):
    """
    A FilteredAggregation computes the sum of columns in the collective dataset for a set of filtered identifiers.

    In this computation, one participant -- the identifier provider -- shares a list of acceptable identifiers in
    plaintext to other participants. The identifier provider does not otherwise contribute data to the computation.
    All other instances filter out records whose identifiers are not in the list, then run a collective aggregation
    for selected columns on all remaining (acceptable) records. This computation can be seen as the combination of
    a set intersection and an aggregation, except the list of acceptable identifiers is not assumed to be sensitive.

    To illustrate this, consider the following configuration, with 3 participants:

      - parameters: `columns = ["x"], identifier="id", identifier_provider="participant_1"`
      - participant_1: `data = [["id"], ["a"], ["b"]]`
      - participant_2: `data = [["id", "x"], ["a", 1], ["c", 5]]`
      - participant_3: `data = [["id", "x"], ["b", 2], ["d", 7], ["e", 9]]`

    To begin with, participant_1 sends `["a", "b"]` to all other participants. Then, participants 2 and 3 filter
    out records whose identifier `id` is not in that list. In this case, we then have

      - participant_2: `filtered_data = [["id", "x"], ["a", 1]]`
      - participant_3: `filtered_data = [["id", "x"], ["b", 2]]`

    Finally, a collective aggregation is run for column `x`, leading to the a sum of 3.

    The dataset of the identifier provider can have additional columns (even `x`), but the values in these columns
    is not used in the aggregation. Also, identifiers are not required to be unique, so participants 2 and 3 could
    have records with the same identifier, which would then be counted twice.

    """

    def __init__(
        self,
        project: "Project",
        columns: list[str],
        identifier: str,
        identifier_provider: str,
        per_instance_breakdown: bool = False,
        dp_epsilon: float = UNSET,
    ):
        """Creates a FilteredAggregation computation on this project.

        Args:
            project (Project): The project to run this computation on.
            columns (list[str]): the columns to aggregate over.
            identifier (str): the name of the column containing the identifiers.
            identifier_provider (str): the name of the instance responsible for providing identifiers.
            per_instance_breakdown (bool, optional): whether to also disaggregate the global count by instance. Defaults to False.
            dp_epsilon (float, optional): When using differential privacy, the budget used by this computation. Defaults to UNSET.
        """
        super().__init__(
            project=project,
            model_class=models.FilteredAggregation,
            columns=[models.ColumnProperties(name=c) for c in columns],
            identifier=identifier,
            identifier_provider=identifier_provider,
            per_instance_breakdown=per_instance_breakdown,
            type=models.ComputationType.FILTEREDAGGREGATION,
            dp_epsilon=dp_epsilon,
        )

    def _process_results(self, results: List[DataContent]) -> float:
        """Processes the results in the same way as Aggregation (without grouping parameters)."""
        result = results[0].get_float_matrix()
        totals = result.data[0]
        if len(result.columns) == len(totals):
            data = {"Column": result.columns, "Total": totals}
        else:
            data = totals
        return pd.DataFrame(data)

    @classmethod
    def from_model(cls, project: "Project", model: models.FilteredAggregation):
        model = models.FilteredAggregation.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                columns=model.columns,
                identifier=model.identifier,
                identifier_provider=model.identifier_provider,
                per_instance_breakdown=false_if_unset(model.per_instance_breakdown),
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return super().from_model(project, model)
