from typing import Any, List, Callable, TypeVar
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk import Client
from tuneinsight.api.sdk.types import UNSET
from tuneinsight.api.sdk.types import  Response
from tuneinsight.api.sdk.api.api_computations import compute
from tuneinsight.api.sdk.api.api_computations import get_computation
from tuneinsight.api.sdk.api.api_dataobject import get_data_object
from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject
import tuneinsight.utils.time_tools as time

ComputationLauncher = TypeVar("ComputationLauncher",bound=Callable[[models.ComputationDefinition,bool],models.Computation])

# @attr.s(auto_attribs=True)
class ComputationRunner():

    client: Client
    project_id: str
    preprocessing: PreprocessingBuilder = None
    datasource: QueryBuilder
    max_timeout: int
    polling_initial_interval: int
    max_sleep_time: int


    def __init__(self, project_id:str = "", client:Client = UNSET):
        self.client = client
        self.project_id = project_id
        self.preprocessing = PreprocessingBuilder()
        self.datasource = QueryBuilder()
        self.max_timeout = 600 * time.second
        self.polling_initial_interval = 100 * time.millisecond
        self.max_sleep_time = 30 * time.second


    def field_is_set(self,field: Any) -> bool:
        if field is UNSET or field == "":
            return False
        return True


    def update_computation_input(self,comp: models.ComputationDefinition):
        if comp.type == models.ComputationType.COLLECTIVEKEYSWITCH:
            return
        if self.datasource.query_set:
            comp.data_source_parameters = self.datasource.get_parameters()
        else:
            if not self.field_is_set(comp.input_data_object):
                comp.data_source_parameters = models.ComputationDataSourceParameters()


    def update_computation_fields(self,comp: models.ComputationDefinition):
        comp.wait = False
        if not self.field_is_set(comp.project_id):
            comp.project_id = self.project_id
        comp.timeout = int(self.max_timeout / time.second)
        self.update_computation_input(comp=comp)


    def is_done(self,comp: models.Computation) -> bool:
        waiting = comp.status not in (models.ComputationStatus.ERROR, models.ComputationStatus.SUCCESS)
        return not waiting

    def refresh(self,comp: models.Computation) -> models.Computation:
        response: Response[models.Computation] = get_computation.sync_detailed(client=self.client,computation_id=comp.id)
        validate_response(response)
        return response.parsed

    def poll_computation(self,comp: models.Computation) -> List[DataObject]:
        # define initial sleeping time and start time
        timeStart = time.now()
        sleep_time = self.polling_initial_interval
        current_comp = comp

        # Poll the computation until done
        while not self.is_done(current_comp):
            if time.since(timeStart) > self.max_timeout:
                raise Exception("computation timeout")
            time.sleep(sleep_time)
            current_comp = self.refresh(comp)
            if sleep_time < self.max_sleep_time:
                sleep_time = int(sleep_time * 1.05)

        # Raise an exception if there is an error
        if (current_comp.status == models.ComputationStatus.ERROR) or (len(comp.error) > 0):
            raise Exception(f"computation error: {current_comp.error}")

        if len(current_comp.results) < 1:
            raise Exception("computation has no results")

        # Get Result models
        results : List[DataObject] = []
        for doID in current_comp.results:
            response: Response[models.DataObject] = get_data_object.sync_detailed(client=self.client,data_object_id=doID)
            validate_response(response)
            results.append(DataObject(model=response.parsed,client=self.client))
        return results

    def key_switch(self,dataObject: DataObject) -> DataObject:
        ksDef = models.CollectiveKeySwitch(type=models.ComputationType.COLLECTIVEKEYSWITCH,cipher_vector=dataObject.get_id(),local=False)
        computation = self.launch_computation(comp=ksDef,local=False)
        return self.poll_computation(computation)[0]


    def launch_computation(self,comp:models.ComputationDefinition,local:bool=False) -> models.Computation:
        comp.local = local
        self.update_computation_fields(comp=comp)
        response : Response[models.Computation] = compute.sync_detailed(client=self.client,json_body=comp)
        validate_response(response)
        return response.parsed

    def post_preprocessing(self, comp: models.ComputationDefinition):
        self.preprocessing.check_validity()

        if comp.preprocessing_parameters == UNSET:
            comp.preprocessing_parameters = models.ComputationPreprocessingParameters()

        if self.preprocessing.chain != []:
            comp.preprocessing_parameters.global_preprocessing = models.PreprocessingChain(self.preprocessing.chain)
        if self.preprocessing.compound_chain != {}:
            compound_params =  models.ComputationPreprocessingParametersCompoundPreprocessing()
            compound_params.additional_properties = self.preprocessing.compound_chain
            comp.preprocessing_parameters.compound_preprocessing = compound_params



    def run_computation(self,comp: models.ComputationDefinition,local: bool=False,keyswitch: bool=True,decrypt: bool=True) -> List[DataObject]:
        self.post_preprocessing(comp)
        computation = self.launch_computation(comp,local=local)
        results = self.poll_computation(comp=computation)


        if keyswitch:
            for i,dataobject in enumerate(results):
                results[i] = self.key_switch(dataobject)
                if decrypt:
                    results[i] = results[i].decrypt()
        return results
