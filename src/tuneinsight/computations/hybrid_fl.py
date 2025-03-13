"""
Classes for Hybrid Federated Learning.

🧪 This is an experimental feature. If your use case involves HybridFL on
   a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.
"""

from typing import Optional, Dict, Union, List
import json
from copy import deepcopy
import pandas as pd
from tuneinsight.client.dataobject import DataContent
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils import deprecation, hybrid_fl_plots


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
        project,
        params: models.HybridFLGenericParams = UNSET,
        spec_params: models.HybridFLSpecParams = UNSET,
        dp_params: models.HybridFLDpParams = UNSET,
        task_id: str = None,
        task_def: Optional[Dict[str, Union[str, int, float]]] = None,
        dp_epsilon: Optional[float] = UNSET,
    ):
        """
        Creates a HybridFL Computation.

        Args:
            project (`Project`): The project to run the computation with.
            params (models.HybridFLGenericParams): the base parameters for this computation.
            spec_params (models.HybridFLSpecParams): the specific parameters for this computation depending on the hybrid FL type.
            dp_params (models.HybridFLDpParams): the differential privacy parameters.
            task_id (str): a unique identifier for this learning task.
            dp_epsilon (float, optional):
                The privacy budget to use with this workflow. Defaults to UNSET, in which case differential privacy is not used.
            task_def (dict): task definition dictionary. See documentation for more details.

        """

        spec_params = self._set_spec_params_type(spec_params)
        super().__init__(
            project,
            models.HybridFL,
            type=models.ComputationType.HYBRIDFL,
            params=params,
            dp_params=dp_params,
            spec_params=spec_params,
            task_id=task_id,
            task_def=json.dumps(task_def) if task_def is not None else UNSET,
            dp_epsilon=dp_epsilon,
        )

    def create_from_params(
        self,
        params: models.HybridFLGenericParams = UNSET,
        spec_params: models.HybridFLSpecParams = UNSET,
        dp_params: models.HybridFLDpParams = UNSET,
        task_id: str = None,
        task_def: Optional[Dict[str, Union[str, int, float]]] = None,
    ):
        deprecation.warn("create_from_params", "HybridFL.__init__")

        model = models.HybridFL(type=models.ComputationType.HYBRIDFL)
        model.params = params

        model.spec_params = spec_params
        model.dp_params = dp_params
        model.task_id = task_id

        if task_def is not None:
            model.task_def = json.dumps(task_def)

        model.project_id = self.project.get_id()

        dataobjects = super().run(local=False)

        return dataobjects

    @classmethod
    def from_model(cls, project: "Project", model: models.HybridFL) -> "HybridFL":
        model = models.HybridFL.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                params=model.params,
                spec_params=model.spec_params,
                dp_params=model.dp_params,
                task_id=model.task_id,
                task_def=model.task_def,
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp

    def _set_spec_params_type(self, spec_params):
        """Sets the spec_params type filed based on the used spec_params."""
        if isinstance(spec_params, models.HybridFLCommunityDetectionParams):
            spec_params.params_type = (
                models.HybridFLParamsType.HYBRIDFLCOMMUNITYDETECTIONPARAMS
            )
        elif isinstance(spec_params, models.HybridFLMachineLearningParams):
            spec_params.params_type = (
                models.HybridFLParamsType.HYBRIDFLMACHINELEARNINGPARAMS
            )
        else:
            spec_params.params_type = models.HybridFLParamsType.HYBRIDFLSPECBASEPARAMS
        return spec_params

    @staticmethod
    def get_results(history, local_only=False):
        """Extracts results from a history dictionary."""
        history = deepcopy(history)
        _format_history(history)
        train_metrics = (
            history.metrics["train"] if local_only else history.init_metrics["train"]
        )
        test_metrics = (
            history.metrics["val"] if local_only else history.init_metrics["val"]
        )

        for key, value in train_metrics.items():
            train_metrics[key] = (
                round(value[-1][-1] or -1, 4)
                if local_only
                else round(value[-1] or -1, 4)
            )
        for key, value in test_metrics.items():
            test_metrics[key] = (
                round(value[-1][-1] or -1, 4)
                if local_only
                else round(value[-1] or -1, 4)
            )

        return train_metrics, test_metrics

    def display_results(self, history, local_only=False, metrics_to_display=("acc",)):
        """Displays the results of this computation, given its history."""
        history = deepcopy(history)
        _format_history(history)

        hybrid_fl_plots.plot_timeline(
            history, local_only=local_only, metrics_to_display=metrics_to_display
        )

    def _process_results(self, results: List[DataContent]) -> pd.DataFrame:
        return results[0].get_ml_result()


def _format_history(history):
    metrics = {}
    for json_metrics in history.metrics:
        round_metrics = json.loads(json_metrics)
        for split, metrics_split in round_metrics.items():
            if split not in metrics:
                metrics[split] = {}
            for key, metrics_array in metrics_split.items():
                if key in metrics[split]:
                    metrics[split][key].append(metrics_array)
                else:
                    metrics[split][key] = [metrics_array]
    history.metrics = metrics

    init_metrics = {}
    for json_metrics in history.init_metrics:
        round_metrics = json.loads(json_metrics)
        for split, metrics_split in round_metrics.items():
            if split not in init_metrics:
                init_metrics[split] = {}
            for key, metrics_array in metrics_split.items():
                if key in init_metrics[split]:
                    init_metrics[split][key].append(metrics_array)
                else:
                    init_metrics[split][key] = [metrics_array]
    history.init_metrics = init_metrics
