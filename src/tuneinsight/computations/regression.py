"""
Encrypted training and evaluation of regressions.

🧪 Encrypted regression is an experimental feature. Only use with small datasets,
as this can take a lot of time and memory. If your use case involves a regression
on a large scale dataset, contact us at contact@tuneinsight.com.

"""

import time
import itertools
import uuid
from typing import List, Dict
from typing_extensions import Self
import pandas as pd

from tuneinsight.client.dataobject import DataContent
from tuneinsight.client.datasource import DataSource
from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.utils.model_performance_eval import r2_score, rmse

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models.encrypted_regression_params import (
    EncryptedRegressionParams,
)


class _RegressionTraining(ModelBasedComputation):
    """A computation that trains a regression."""

    def __init__(self, project, regression_type):
        self.params = EncryptedRegressionParams(type=regression_type, seed=0)
        super().__init__(
            project,
            models.EncryptedRegression,
            type=models.ComputationType.ENCRYPTEDREGRESSION,
            params=self.params,
        )

    def _process_results(self, results: List[DataContent]) -> str:
        return results[0].get_id()

    def _process_encrypted_results(self, results: List[DataContent]) -> str:
        return results[0].get_id()


class _RegressionPredicting(ModelBasedComputation):
    """A computation that evaluates a regression over some inputs."""

    def __init__(self, project):
        super().__init__(
            project,
            models.EncryptedPrediction,
            type=models.ComputationType.ENCRYPTEDPREDICTION,
        )

    def _process_results(self, results: List[DataContent]) -> bytes:
        return results[0].get_float_matrix()

    def _process_encrypted_results(self, results: List[DataContent]) -> bytes:
        return results[0].get_raw_data()


class Regression:
    """
    Regression computations interface.

    This class enables the training and evaluation of an encrypted regression model.
    Note that this class is not itself a Computation, but more a "manager" for two
    different computation classes (since fit and predict are two different computations).

    🧪 This is an experimental feature. Only use with small datasets, as this can take
    a lot of time and memory. If your use case involves a regression on a large scale
    dataset, contact us at contact@tuneinsight.com.

    """

    fit_model: models.EncryptedRegression
    predict_model: models.EncryptedPrediction
    encrypted_model_dataobject_id: str
    regression_type: models.RegressionType

    def __init__(
        self,
        reg_type: models.RegressionType,
        project: "Project",
    ):
        self.project = project
        self.regression_type = reg_type
        self.fit_model = _RegressionTraining(project, reg_type)
        self.predict_model = _RegressionPredicting(project)
        self.fit_model["timeout"] = 500

    def copy(self):
        return type(self)(self.regression_type, self.project)

    def fit(
        self,
        X: List[str],
        y: List[str],
        learning_rate=0.02,
        network_iteration_count=1,
        seed=0,
        elastic=0.85,
        momentum=0.92,
    ) -> Self:
        """
        Trains the regression model.

        Args:
            X (List[str]): Column names of the features
            y (List[str]): Column names of the labels
            learning_rate (float, optional): The learning rate of the regression. Defaults to 0.02.
            network_iteration_count (int, optional): The global maximum number of iterations. Defaults to 1.
            seed (int, optional): The seed to sample the initial weights. Defaults to 0.
            elastic (float, optional): The elastic rate of the regression. Defaults to 0.85.
            momentum (float, optional):The momentum rate of the regression. Defaults to 0.92.

        Returns:
            self: this object.
        """
        self.fit_model["feature_columns"] = X
        self.fit_model["label_columns"] = y
        self.fit_model.params.learning_rate = learning_rate
        self.fit_model.params.network_iteration_count = network_iteration_count
        self.fit_model.params.seed = seed
        self.fit_model.params.elastic_rate = elastic
        self.fit_model.params.momentum = momentum
        # Run this model, which returns the ID of the result.
        self.encrypted_model_dataobject_id = self.fit_model.run(
            local=False, keyswitch=False, decrypt=False
        )

        return self

    def predict(self, X: pd.DataFrame) -> models.FloatMatrix:
        """
        Predicts the target class for attributes X using the model.

        Args:
            X (pd.DataFrame): Test data

        Returns:
            models.FloatMatrix: Predicted labels
        """
        # Create a dataobject holding the data to predict for.
        ds_uid = uuid.uuid4()
        ds = DataSource.from_dataframe(
            client=self.project.client, dataframe=X, name="predict_data_" + str(ds_uid)
        )
        do = ds.adapt(models.DataObjectType.TABLE)
        ds.delete()

        # Setup the parameters of the prediction model.
        self.predict_model["model"] = self.encrypted_model_dataobject_id
        self.predict_model["data"] = do.get_id()
        self.predict_model["feature_columns"] = self.fit_model["feature_columns"]
        self.predict_model["only_root_prediction"] = True

        # run predict comp
        # self.fit_model = self.predict_model
        return self.predict_model.run(local=False, release=False)

    def grid_search(
        self,
        feature_cols: List[str],
        label_cols: List[str],
        test_X: pd.DataFrame,
        test_Y: pd.DataFrame,
        param_dict: dict = None,
        log: bool = False,
    ) -> dict:
        """
        Performs a grid search on model parameters to fine-tune the model

        Args:
            feature_cols (List[str]): Column names of the features
            label_cols (List[str]): Column names of the labels
            test_X (pd.DataFrame): Test data features
            test_Y (pd.DataFrame): Test data labels
            param_dict (dict, optional): dictionary of parameters to test. Defaults to None.
            log (bool, optional): Whether or not to log intermediate results. Defaults to False.

        Returns:
            dict: dictionary of the combination of parameters with the highest R2 score
        """
        if param_dict is None:
            param_dict = {
                "learning_rate": [0.004, 0.005],
                "network_iteration_count": [1, 2],
                "elastic": [0.85, 0.98],
            }
        param_grid = self._generate_param_grid(param_dict)
        default_params = {
            "learning_rate": 0.0045,
            "elastic": 0.85,
            "seed": 0,
            "momentum": 0.92,
            "network_iteration_count": 1,
        }

        start_time = time.time()

        best_r2 = float("-inf")
        rmse_of_best = float("inf")
        best_params = default_params
        for params in param_grid:
            all_params = dict(default_params | params)
            if log:
                print("Parameters:")
                for param, val in all_params.items():
                    print("  " + param + ": " + str(val))

            regression = self.copy()

            model = regression.fit(
                feature_cols,
                label_cols,
                learning_rate=all_params["learning_rate"],
                elastic=all_params["elastic"],
                seed=all_params["seed"],
                momentum=all_params["momentum"],
                network_iteration_count=all_params["network_iteration_count"],
            )
            results = model.predict(X=test_X)
            predictions = [
                pred
                for prediction_list in results.predictions
                for pred in prediction_list
            ]
            r2_tmp = r2_score(test_Y, predictions)
            rmse_tmp = rmse(test_Y, predictions)

            if r2_tmp > best_r2:
                best_r2 = r2_tmp
                best_params = all_params
                rmse_of_best = rmse_tmp

            if log:
                print("R2 Score: " + str(r2_tmp))
                print("RMSE: " + str(rmse_tmp))
                print(f"-------- {time.time() - start_time} seconds -------")
                start_time = time.time()

        print("Best hyper-parameters:")
        for param, val in best_params.items():
            print("  " + param + ": " + str(val))
        print("R2 Score: " + str(best_r2))
        print("RMSE: " + str(rmse_of_best))

        return best_params

    @staticmethod
    def _generate_param_grid(param_dict: Dict) -> List[dict]:
        """
        Generates a grid of parameter combinations

        Args:
            param_dict (dict): dictionary of different parameter values to include in the parameter grid

        Returns:
            list[dict]: list of all parameter combinations
        """
        keys = param_dict.keys()
        values = (param_dict[key] for key in keys)
        return [
            dict(zip(keys, combination)) for combination in itertools.product(*values)
        ]


class LinearRegression(Regression):
    """Linear Regression (🧪 experimental feature)"""

    type: models.RegressionType = models.RegressionType.LINEAR

    continuous_labels: bool

    def __init__(self, project: "Project", continuous_labels: bool):
        """
        Args
            continuous_labels (bool): If true, then expects continuous labels (i.e. not binary).

        """
        super().__init__(reg_type=self.type, project=project)
        self.continuous_labels = continuous_labels
        self.fit_model.params.linear = models.EncryptedRegressionParamsLinear(
            continuous_labels=continuous_labels
        )

    def copy(self):
        return type(self)(self.project, self.continuous_labels)


class LogisticRegression(Regression):
    """Logistic Regression (🧪 experimental feature)"""

    type: models.RegressionType = models.RegressionType.LOGISTIC

    approximation_params: models.approximation_params.ApproximationParams

    def __init__(
        self,
        project: "Project",
        approximation_params: models.approximation_params.ApproximationParams,
    ):
        """
        Args:
            approximation_params: parameters of the sigmoid approximation.

        """
        super().__init__(reg_type=self.type, project=project)
        self.fit_model.params.approximation_params = self.approximation_params = (
            approximation_params
        )

    def copy(self):
        return type(self)(self.project, self.approximation_params)


class PoissonRegression(Regression):
    """Poisson Regression (🧪 experimental feature)"""

    type: models.RegressionType = models.RegressionType.POISSON

    def __init__(self, project: "Project"):
        super().__init__(reg_type=self.type, project=project)
