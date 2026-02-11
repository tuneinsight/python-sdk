"""
Classes to train and evaluate machine learning models in a Tune Insight instance.

🧪 Encrypted machine learning is an experimental feature. Only use with small datasets,
   as this can take a lot of time and memory. If your use case involves machine learning
   on a large scale dataset, contact us at contact@tuneinsight.com.

🚧 This module is in active development, and likely to change dramatically in the next
   few releases. Use with caution.

"""

from enum import Enum

from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.models import Model as APIModel
from tuneinsight.api.sdk.models import (
    RegressionType,
    SessionDefinition,
    Session,
    DataObjectType,
    KeyInfo,
)
from tuneinsight.api.sdk.api.api_ml import (
    get_model,
    delete_model,
)
from tuneinsight.api.sdk.api.api_sessions import post_session
from tuneinsight.client.validation import validate_response
from tuneinsight.cryptolib.cryptolib import (
    new_hefloat_operator_from_b64_scheme_context,
    get_relin_key_bytes,
)
from tuneinsight.computations.regression import _RegressionPredicting
from tuneinsight.client.dataobject import DataObject
from tuneinsight.api.sdk.types import Response
from tuneinsight.utils import deprecation


class ModelType(Enum):
    """
    The different types of machine learning models.
    """

    LINEAR = RegressionType.LINEAR
    LOGISTIC = RegressionType.LOGISTIC
    POISSON = RegressionType.POISSON


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
        deprecation.warn("Model (and Maas in general)", breaking=True)

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
