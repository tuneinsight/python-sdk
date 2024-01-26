from typing import List, Dict
import pandas as pd
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.computations.survival import SurvivalParameters
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.types import UNSET


class SurvivalAggregation(ComputationRunner):
    subgroups: List[models.SurvivalAggregationSubgroupsItem]
    matching_organization: str
    secure_matching: bool
    matching_columns: List[models.MatchingColumn]

    def __init__(self, project_id: str = "", client: Client = UNSET):
        self.subgroups = []
        self.secure_matching = False
        self.matching_organization = ""
        self.matching_columns = []
        super().__init__(project_id, client)

    def add_categories(self, column: str, values: List[str]):
        for v in values:
            self.add_subgroup(v, column, models.ComparisonType.EQUAL, v)

    def add_subgroup(
        self,
        name: str,
        target_column: str,
        comparator: models.ComparisonType,
        value: str,
        numerical: bool = False,
    ):
        filter_operation = models.Filter(
            type=models.PreprocessingOperationType.FILTER,
            col_name=target_column,
            comparator=comparator,
            value=value,
            numerical=numerical,
        )
        item = models.SurvivalAggregationSubgroupsItem(
            filter_=filter_operation, name=name
        )
        self.subgroups.append(item)

    def set_matching(
        self,
        matching_organization: str,
        matching_columns: List[str],
        fuzzy_matching: bool = False,
    ):
        self.secure_matching = True
        self.matching_columns = []
        self.matching_organization = matching_organization
        for c in matching_columns:
            self.matching_columns.append(
                models.MatchingColumn(name=c, fuzzy=fuzzy_matching)
            )

    def compute_survival(
        self, survival_parameters: SurvivalParameters
    ) -> Dict[str, pd.DataFrame]:
        # Set parameters and run computation
        model = models.SurvivalAggregation(
            type=models.ComputationType.SURVIVALAGGREGATION
        )
        model.subgroups = self.subgroups
        model.secure_matching = self.secure_matching
        model.matching_columns = self.matching_columns
        model.matching_organization = self.matching_organization
        model.project_id = self.project_id
        model.survival_parameters = survival_parameters.get_preprocessing_op()
        dataobjects = super().run_computation(comp=model, local=False, release=True)
        # Compute Mapping for survival results
        fm = dataobjects[0].get_float_matrix()
        if len(fm.data) != len(self.subgroups) + 1:
            raise Exception(
                f"result dimensions mismatch, expected {len(self.subgroups) + 1} rows, got {len(fm.data)}"
            )
        result_mapping = {}
        for i, row in enumerate(fm.data):
            subgroup_name = "all"
            if i > 0:
                subgroup_name = self.subgroups[i - 1].name
            df = pd.DataFrame({"Column": fm.columns, "Total": row})
            result_mapping[subgroup_name] = survival_parameters.compute_survival(df)
        return result_mapping
