"""
Classes for Secure Inference.

🧪 This is an experimental feature. If your use case involves Secure Inference on
   a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.
"""

from typing import List
import pandas as pd
from tuneinsight.client.dataobject import DataContent
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils import deprecation


class SecureInference(ModelBasedComputation):
    """
    Secure Inference to run inference on encrypted data.

    In Secure Inference, the leaves nodes send encrypted tabular data to a central server,
    which performs inference on the data without ever decrypting it. The results are then sent back
    to the leaves nodes, which decrypt them locally.
    """

    def __init__(
        self,
        project,
        model_name: str = UNSET,
        batch_size: int = UNSET,
    ):
        """
        Creates a Secure Inference Computation.

        Args:
            project (`Project`): The project to run the computation with.
            model_name (str): The name of the model to use for inference.
            batch_size (int): The batch size to use for inference.
        """

        super().__init__(
            project,
            models.SecureInference,
            type=models.ComputationType.SECUREINFERENCE,
            model_name=model_name,
            batch_size=batch_size,
        )

    def create_from_params(
        self,
        model_name: str = UNSET,
        batch_size: int = UNSET,
    ):
        deprecation.warn("create_from_params", "SecureInference.__init__")

        model = models.SecureInference(type=models.ComputationType.SECUREINFERENCE)
        model.model_name = model_name
        model.batch_size = batch_size

        model.project_id = self.project.get_id()

        dataobjects = super().run(local=False)

        return dataobjects

    @classmethod
    def from_model(
        cls, project: "Project", model: models.SecureInference
    ) -> "SecureInference":
        model = models.SecureInference.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                model_name=model.model_name,
                batch_size=model.batch_size,
            )
        comp._adapt(model)
        return comp

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        return results[0].get_dataframe()
