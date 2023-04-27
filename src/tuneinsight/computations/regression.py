import time
import itertools
import uuid
from typing import List,Dict
from typing_extensions import Self
import pandas as pd
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.models.computation_type import ComputationType
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.models.encrypted_regression_params import EncryptedRegressionParams
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.client.computations import ComputationRunner
from tuneinsight.client.datasource import DataSource
from tuneinsight.utils.model_performance_eval import r2_score, rmse


class Regression(ComputationRunner):
    """ Regression computation

    """

    feature_columns: List[str]
    label_columns: List[str]
    model: models.EncryptedRegression
    predict_model : models.EncryptedPrediction
    encrypted_model_dataobject_id: str
    type: models.RegressionType


    def __init__(self, reg_type: models.RegressionType, client:Client = UNSET, project_id:str=""):
        self.type = reg_type
        self.model = models.EncryptedRegression(type=models.ComputationType.ENCRYPTEDREGRESSION)
        self.predict_model = models.EncryptedPrediction(type=ComputationType.ENCRYPTEDPREDICTION)
        self.model.params = EncryptedRegressionParams(type=reg_type, seed=0)
        super().__init__(client=client, project_id=project_id)
        self.max_timeout = self.max_timeout * 10
        self.model.timeout = 500

    def copy(self):
        return type(self)(self.type, self.client, self.project_id)


    def fit(self, X: List[str], y: List[str], learning_rate=0.02, network_iteration_count=1, seed=0, elastic=0.85, momentum=0.92) -> Self:
        """ Fit the regression model

        Args:
            X (List[str]): Column names of the features
            y (List[str]): Column names of the labels
            learning_rate (float, optional): The learning rate of the regression. Defaults to 0.02.
            network_iteration_count (int, optional): The global maximum number of iterations. Defaults to 1.
            seed (int, optional): The seed to sample the initial weights. Defaults to 0.
            elastic (float, optional): The elastic rate of the regression. Defaults to 0.85.
            momentum (float, optional):The momentum rate of the regression. Defaults to 0.92.

        Returns:
            Self: Fitted model
        """
        self.model.feature_columns = X
        self.model.label_columns = y
        self.model.params.learning_rate = learning_rate
        self.model.params.network_iteration_count = network_iteration_count
        self.model.params.seed = seed
        self.model.params.elastic_rate = elastic
        self.model.params.momentum = momentum

        dataobjects = super().run_computation(comp=self.model, local = False, keyswitch=False, decrypt=False)

        self.encrypted_model_dataobject_id = dataobjects[0].get_id()

        return self


    def predict(self, X: pd.DataFrame) -> models.FloatMatrix:
        """  Predict using the model

        Args:
            X (pd.DataFrame): Test data

        Returns:
            models.FloatMatrix: Predicted labels
        """
        # set predict params
        self.predict_model.model = self.encrypted_model_dataobject_id

        ds_uid = uuid.uuid4()
        ds = DataSource.from_dataframe(client=self.client,dataframe=X, name="predict_data_"+str(ds_uid))
        do = ds.adapt(models.DataObjectType.TABLE)
        ds.delete()
        self.predict_model.data = do.get_id()

        self.predict_model.feature_columns = self.model.feature_columns
        self.predict_model.only_root_prediction = True

        # run predict comp
        dataobjects = super().run_computation(comp=self.predict_model, local=False, keyswitch=True, decrypt=True)
        return dataobjects[0].get_float_matrix()

    def grid_search(self, feature_cols: List[str], label_cols: List[str], test_X: pd.DataFrame, test_Y:pd.DataFrame, param_dict:dict = None, log:bool = False) -> dict:
        """ Performs a grid search on parameters to fine-tune the model

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
            param_dict = {'learning_rate': [0.004, 0.005], 'network_iteration_count':[1, 2], 'elastic':[0.85, 0.98]}
        param_grid = self.generate_param_grid(param_dict)
        default_params = {'learning_rate': 0.0045, 'elastic':0.85, 'seed':0, 'momentum':0.92, 'network_iteration_count':1}



        start_time = time.time()

        best_r2 = float('-inf')
        rmse_of_best = float('inf')
        best_params = default_params
        for params in param_grid:
            all_params = dict(default_params | params)
            if log:
                print("Parameters:")
                for param,val in all_params.items():
                    print("  " + param + ": " + str(val))

            regression = self.copy()

            model = regression.fit(feature_cols,label_cols, learning_rate=all_params['learning_rate'], elastic=all_params['elastic'], seed=all_params['seed'], momentum=all_params['momentum'], network_iteration_count=all_params['network_iteration_count'])
            results = model.predict(X=test_X)
            predictions = [pred for prediction_list in results.predictions for pred in prediction_list]
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
        for param,val in best_params.items():
            print("  " + param + ": " + str(val))
        print("R2 Score: " + str(best_r2))
        print("RMSE: " + str(rmse_of_best))

        return best_params

    @staticmethod
    def generate_param_grid(param_dict:Dict) -> List[dict]:
        """ Generates a grid of parameter combinations

        Args:
            param_dict (dict): dictionary of different parameter values to include in the parameter grid

        Returns:
            list[dict]: list of all parameter combinations
        """
        keys = param_dict.keys()
        values = (param_dict[key] for key in keys)
        return [dict(zip(keys, combination)) for combination in itertools.product(*values)]


class LinearRegression(Regression):
    """ Linear Regression
    """
    type: models.RegressionType = models.RegressionType.LINEAR

    continuous_labels: bool

    def __init__(self, continuous_labels: bool, client:Client = UNSET, project_id:str=""):
        super().__init__(reg_type=self.type, client=client, project_id=project_id)
        self.continuous_labels = continuous_labels
        self.model.params.linear = models.EncryptedRegressionParamsLinear(continuous_labels=continuous_labels)

    def copy(self):
        return type(self)(self.continuous_labels, self.client, self.project_id)

class LogisticRegression(Regression):
    """ Logistic Regression
    """
    type: models.RegressionType = models.RegressionType.LOGISTIC

    approximation_params: models.approximation_params.ApproximationParams

    def __init__(self, approximation_params:models.approximation_params.ApproximationParams, client:Client = UNSET, project_id:str=""):
        super().__init__(reg_type=self.type, client=client, project_id=project_id)
        self.model.params.approximation_params = approximation_params

class PoissonRegression(Regression):
    """Poisson Regression
    """
    type: models.RegressionType = models.RegressionType.POISSON

    def __init__(self, client:Client = UNSET, project_id:str=""):
        super().__init__(reg_type=self.type, client=client, project_id=project_id)
