"""
Classes to train and evaluate machine learning models in a Tune Insight instance.

🧪 Encrypted machine learning is an experimental feature. Only use with small datasets,
   as this can take a lot of time and memory. If your use case involves machine learning
   on a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.

"""

from typing import Any, List
from enum import Enum
import numpy as np

from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.models import Model as APIModel
from tuneinsight.api.sdk.models import (
    RegressionType,
    ModelDefinition,
    PredictionParams,
    ApproximationParams,
    SessionDefinition,
    Session,
    DataObjectType,
    KeyInfo,
)
from tuneinsight.api.sdk.api.api_ml import (
    get_model_list,
    get_model,
    post_model,
    delete_model,
)
from tuneinsight.api.sdk.api.api_sessions import post_session
from tuneinsight.client.validation import validate_response
from tuneinsight.cryptolib.cryptolib import (
    new_hefloat_operator_from_b64_scheme_context,
    get_relin_key_bytes,
    encrypt_prediction_dataset,
    decrypt_prediction,
)
from tuneinsight.computations.regression import _RegressionPredicting
from tuneinsight.client.dataobject import DataObject
from tuneinsight.api.sdk.types import Response
from tuneinsight.utils.io import data_to_bytes, data_from_bytes


class ModelType(Enum):
    """
    The different types of machine learning models.
    """

    LINEAR = RegressionType.LINEAR
    LOGISTIC = RegressionType.LOGISTIC
    POISSON = RegressionType.POISSON


class _EmptyProject:
    """Empty project (necessary to run the MaaS computations)."""

    def __init__(self, client):
        self.client = client

    def get_id(self):
        return ""


class Model:
    """
    A machine learning model stored on the agent.
    """

    client: Client
    model: APIModel

    def __init__(self, client: Client, model: APIModel):
        """
        Initializes the model class given the client and API model.

        Args:
            client (Client): the client used to communicate with the corresponding agent
            model (APIModel): the API model
        """
        self.client = client
        self.model = model

    def __str__(self) -> str:
        """
        __str__ returns a string representation of the mode

        Returns:
            str: the model's string representation
        """
        return f"Model(name={self.model.name}, type={self.model.type}, training algorithm={self.model.training_algorithm})"

    def delete(self):
        """
        delete deletes the model from the agent (can only be done by the model owner)
        """
        resp = delete_model.sync_detailed(
            client=self.client, model_id=self.model.model_id
        )
        validate_response(resp)

    def refresh(self):
        """
        refresh refreshes this local model class with the data stored on the remote agent
        """
        resp: Response[APIModel] = get_model.sync_detailed(
            client=self.client, model_id=self.model.model_id
        )
        validate_response(resp)
        self.model = resp.parsed

    def compute_prediction(self, data: Any, project: "Project" = None) -> np.ndarray:
        """
        Computes an encrypted prediction on the model given the dataset.

        The dataset is first encrypted locally with ephemeral keys and then sent to the agent
        owning the model to compute the prediction homomorphically, the encrypted result is then
        decrypted locally and returned as a numpy array.

        Args:
            data (Any): the dataset to make the prediction on.
            project (Project): the project to run this prediction in.

        Returns:
            np.ndarray: the decrypted predicted values
        """
        if project is None:
            project = _EmptyProject(self.client)

        self.refresh()
        # Create a new session on the agent
        s_id = self._new_session()

        # Generate and upload evaluation keys
        cs_id = self._upload_eval_keys(s_id)

        # encrypt and upload dataset
        ct = self._encrypt_dataset(cs_id, data)
        input_id = self._upload_dataset(s_id, ct)

        # run the prediction computation
        encrypted_pred = self._run_prediction(project, input_id)
        # decrypt the encrypted result
        result_df = self._decrypt_prediction(cs_id, encrypted_pred)

        return result_df

    # Helpers for the prediction

    def _new_session(self) -> str:
        # Create a Session
        sess_def = SessionDefinition(params=self.model.model_params.cryptolib_params)
        sess_resp: Response[Session] = post_session.sync_detailed(
            client=self.client, json_body=sess_def
        )
        validate_response(sess_resp)
        s_id = sess_resp.parsed.id
        return s_id

    def _upload_eval_keys(self, s_id: str) -> bytes:
        # Load the parameters into a cryptosystem
        cs_id = new_hefloat_operator_from_b64_scheme_context(
            str(self.model.model_params.cryptolib_params)
        )
        # Generate and upload relinearization key
        rlk_bytes = get_relin_key_bytes(cs_id)
        key_info = KeyInfo(collective=False)
        do_type = DataObjectType.RLWE_RELINEARIZATION_KEY
        DataObject.create(
            client=self.client,
            do_type=do_type,
            session_id=s_id,
            encrypted=False,
            key_info=key_info,
            data=rlk_bytes,
        )
        return cs_id

    def _encrypt_dataset(self, cs_id: bytes, data: Any) -> bytes:
        csv_bytes = data_to_bytes(data, remove_header=True)
        return encrypt_prediction_dataset(
            cs_id, csv_bytes, self.model.model_params.prediction_params, False
        )

    def _upload_dataset(self, s_id: str, ct: bytes) -> str:
        do_type = DataObjectType.ENCRYPTED_PREDICTION_DATASET
        data_object = DataObject.create(
            client=self.client,
            do_type=do_type,
            session_id=s_id,
            encrypted=True,
            data=ct,
        )
        return data_object.model.unique_id

    def _run_prediction(self, project: "Project", input_id: str) -> bytes:
        comp = _RegressionPredicting(project)
        comp["data"] = input_id
        comp["model"] = self.model.data_object.unique_id
        return comp.run(local=True)

    @staticmethod
    def _decrypt_prediction(cs_id: bytes, ct: bytes) -> np.ndarray:
        result = decrypt_prediction(cs_id, ct)
        return np.array(data_from_bytes(result, no_header=True))


class ModelManager:
    """
    Exposes useful methods for interacting with Tune Insight's Machine Learning Models API
    """

    client: Client

    def __init__(self, client: Client):
        """
        __init__ initializes itself given a valid API client

        Args:
            client (Client): the API client
        """
        self.client = client

    @staticmethod
    def _validate_weights(data: List[List[Any]]) -> List[List[float]]:
        try:
            new_data = [[float(element) for element in row] for row in data]
            return new_data
        except Exception as exception:
            raise AttributeError(
                "Could not convert weights to valid float values."
            ) from exception

    def get_models(self) -> List[Model]:
        """
        get_models Returns the list of models stored on the agent

        Returns:
            List[Model]: the list of models
        """
        response: Response[List[APIModel]] = get_model_list.sync_detailed(
            client=self.client
        )
        validate_response(response)
        result = []
        for model in response.parsed:
            result.append(Model(client=self.client, model=model))
        return result

    def get_model(self, model_id: str = "", name: str = "") -> Model:
        """
        get_model returns the model schema given either its model id or the common name, returning the first match found
        if the two arguments are non-empty.

        Args:
            model_id (str, optional): the id of the model to retrieve. Defaults to "".
            name (str, optional): the name of the model to retrieve. Defaults to "".

        Raises:
            AttributeError: if no id or name was given
            NameError: if the requested model cannot be found

        Returns:
            Model: _description_
        """
        if model_id == "" and name == "":
            raise AttributeError(
                "At least one of `model_id` or `name` must be specified."
            )
        models = self.get_models()
        for m in models:
            if model_id != "":
                if m.model.model_id == model_id:
                    return m
            if name != "":
                if m.model.name == name:
                    return m
        raise NameError(f"No model with id={model_id} or name={name} was found.")

    def new_model(
        self,
        name: str,
        regression_type: ModelType,
        data: List[List[Any]],
        delete_if_exists: bool = False,
    ) -> Model:
        """
        Uploads a new model to the agent.

        Args:
            name (str): the common name to give to the model
            regression_type (Type): the type of regression used to train the model.
            data (List[List[Any]]): the weights which should be numerical.
            delete_if_exists (bool, optional): if the model already exists on the backend, then attempts to delete it. Defaults to False.

        Raises:
            AttributeError: if the model name is already taken.

        Returns:
            Model: _description_
        """
        models = self.get_models()
        for m in models:
            if name == m.model.name:
                if delete_if_exists:
                    m.delete()
                else:
                    raise AttributeError(f"A model named {name} already exists.")
        pred_params = PredictionParams()
        pred_params.regression_type = regression_type
        pred_params.approximation_params = ApproximationParams()
        weights = self._validate_weights(data)
        model_definition = ModelDefinition(
            name=name, prediction_params=pred_params, weights=weights
        )
        response: Response[APIModel] = post_model.sync_detailed(
            client=self.client, json_body=model_definition
        )
        validate_response(response)
        return Model(self.client, response.parsed)
