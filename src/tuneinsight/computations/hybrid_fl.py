"""
Classes for Hybrid Federated Learning.

🧪 This is an experimental feature. If your use case involves HybridFL on
   a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.
"""

import base64
from typing import Optional, Union, Sequence, Literal

import pandas as pd

# ti-models is optional; importing HybridFL without the ml extra is handled by
# tuneinsight.computations, while Pylint analyzes this module independently.
# pylint: disable=import-error
from ti_models.trainer.ti_trainer import TITrainer
from ti_models.trainer.training_metadata import (
    TIEventType,
    TrainingMetadata,
    generate_federated_curves,
)

# pylint: enable=import-error

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET, is_set, is_unset
from tuneinsight.client.dataobject import DataContent
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils.plots import (
    style_plot,
    TI_COLORS,
)

MAX_BINARY_TRAINER_SIZE_BYTES = 200_000


class HybridFL(ModelBasedComputation):
    """
    Hybrid Federated Learning to train models collaboratively.

    In Hybrid Federated Learning, each party first performs local updates of a
    shared model, using their own data. Then, these models are aggregated
    together under encryption to obtain a new version of the shared model.

    All the computation and sharing is performed in the backend: this class
    only provides a high-level interface to start a computation and fetch
    results.

    This computation is configured by a data class defined by the API, that
    you should use directly.

    """

    def __init__(
        self,
        project: "Project",  # type: ignore,
        params: models.HybridFLGenericParams = UNSET,
        spec_params: models.HybridFLSpecParams = UNSET,
        dp_params: models.HybridFLDpParams = UNSET,
        trainer: Optional[TITrainer] = UNSET,
        dp_epsilon: Optional[float] = UNSET,
    ):
        """
        Creates a HybridFL Computation.

        Args:
            project (`Project`): The project to run the computation with.
            params (models.HybridFLGenericParams): the base parameters for this computation.
            spec_params (models.HybridFLSpecParams): the specific parameters for this computation depending on the hybrid FL type.
            dp_params (models.HybridFLDpParams): the differential privacy parameters.
            trainer (TITrainer, optional): The trainer defining the model and training procedure. Required if spec_params is of type HybridFLMachineLearningParams.
            dp_epsilon (float, optional):
                The privacy budget to use with this workflow. Defaults to UNSET, in which case differential privacy is not used.
        """
        if is_set(trainer) and trainer is not None:
            creation_event = trainer.metadata.get_latest_event(TIEventType.CREATION)
            if creation_event and not creation_event.author:
                creation_event.author = project.model.created_by_node
        spec_params = self._set_spec_params_type(spec_params, trainer)
        super().__init__(
            project,
            models.HybridFL,
            type=models.ComputationType.HYBRIDFL,
            params=params,
            dp_params=dp_params,
            spec_params=spec_params,
            dp_epsilon=dp_epsilon,
        )

    @classmethod
    def from_model(cls, project: "Project", model: models.HybridFL) -> "HybridFL":
        model = models.HybridFL.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                params=model.params,
                spec_params=model.spec_params,
                dp_params=model.dp_params,
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    def _set_spec_params_type(self, spec_params, trainer: Optional[TITrainer] = UNSET):
        """
        Sets the spec_params type field based on the used spec_params.
        If spec_params is of type HybridFLMachineLearningParams, trainer must be provided.

        Args:
            spec_params (models.HybridFLSpecParams): the specific parameters for this computation depending on the hybrid FL type.
            trainer (TITrainer, optional): The trainer defining the model and training procedure. Required if spec_params is of type HybridFLMachineLearningParams.

        Raises:
            ValueError: If spec_params is of type HybridFLMachineLearningParams and trainer is not provided.
        """
        if isinstance(spec_params, models.HybridFLCommunityDetectionParams):
            spec_params.params_type = (
                models.HybridFLParamsType.HYBRIDFLCOMMUNITYDETECTIONPARAMS
            )
        elif isinstance(spec_params, models.HybridFLMachineLearningParams):
            if is_unset(spec_params.trainer) and (is_unset(trainer) or trainer is None):
                raise ValueError(
                    "Trainer must be provided when using HybridFLMachineLearningParams"
                )
            if is_set(trainer) and trainer is not None:
                binary_trainer = trainer.marshal_binary(is_init_trainer=True)
                if len(binary_trainer) > MAX_BINARY_TRAINER_SIZE_BYTES:
                    raise ValueError(
                        "The serialized trainer must not exceed "
                        f"{MAX_BINARY_TRAINER_SIZE_BYTES} bytes"
                    )
                encoded_trainer = base64.b64encode(binary_trainer).decode()
                spec_params.trainer = encoded_trainer
            spec_params.params_type = (
                models.HybridFLParamsType.HYBRIDFLMACHINELEARNINGPARAMS
            )

        else:
            spec_params.params_type = models.HybridFLParamsType.HYBRIDFLSPECBASEPARAMS
        return spec_params

    def plot_results(
        self,
        result,
        metric_key: str = "loss",
        palette: Optional[Union[str, Sequence]] = None,
        align_by: Literal["step", "time"] = "step",
    ):
        """Plot the training curves from the participants from the result of the computation."""
        if palette is None:
            palette = TI_COLORS

        metadata = TrainingMetadata.unmarshal_json(result.metadata)
        events = metadata.events

        curves = generate_federated_curves(events, metric_key=metric_key)

        style_kwargs = {
            "title": f"{metadata.name.replace('_', ' ')} learning curves",
            "x_label": "",
            "y_label": metric_key,
            "size": (12, 6),
        }

        def style_fn(axis, fig, **kwargs):
            style_plot(axis, fig, **kwargs)

        curves.plot(
            palette=palette,
            show_aggregations=True,
            align_by=align_by,
            style_fn=style_fn,
            style_kwargs=style_kwargs,
        )

    def _process_results(self, results: list[DataContent]) -> pd.DataFrame:
        return results[0].get_ml_result()
