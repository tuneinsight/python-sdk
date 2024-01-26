from typing import Union, List
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.api.sdk.types import UNSET, Unset


class EncryptedMean(ComputationRunner):
    """
    Computes the mean and standard deviation of a list of numbers, removes outliers, then returns the mean without outliers.

    """

    participant: Union[Unset, str] = UNSET
    variables: Union[Unset, List[str]] = UNSET
    grouping_keys: Union[Unset, List[str]] = UNSET
    min_participants: Union[Unset, int] = 5
    outlier_threshold: Union[Unset, float] = 2

    def __init__(self, project_id: str = "", client=UNSET):
        super().__init__(project_id=project_id, client=client)

    def get_model(self) -> models.EncryptedMean:
        """
        get_model initializes the computation definition given the parameters of this class

        Returns:
            models.EncryptedMean: the API model for the computation definition
        """
        model = models.EncryptedMean(type=models.ComputationType.ENCRYPTEDMEAN)
        model.project_id = self.project_id
        model.participant = self.participant
        model.grouping_keys = self.grouping_keys
        model.min_participants = self.min_participants
        model.outlier_threshold = self.outlier_threshold
        model.variables = self.variables
        return model

    def compute_average(self, local: bool = False) -> pd.DataFrame:
        """
        compute_average runs the secure average computation.

        Args:
            local (bool, optional): defines whether the computation is run locally or collectively. Defaults to False.

        Returns:
            pd.DataFrame: the resulting dataset that contains all of the averages
        """
        model = self.get_model()
        return (
            super()
            .run_computation(comp=model, local=local, release=True)[0]
            .get_dataframe()
        )
