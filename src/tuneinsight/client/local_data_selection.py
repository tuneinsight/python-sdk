
from typing import Callable
from tuneinsight.api.sdk.models import LocalDataSelection as SelectionModel
from tuneinsight.api.sdk.models import LocalDataSelectionDefinition as DefinitionModel
from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder



class LocalDataSelection:
    '''
    Represents a data selection it comprises of both data source and preprocessing parameters
    '''


    update_func: Callable[[DefinitionModel],SelectionModel]
    preprocessing: PreprocessingBuilder = None
    datasource: QueryBuilder = None
    description: str = ""
    name: str = ""


    def __init__(self,
                 update: Callable[[DefinitionModel],SelectionModel],
                 name: str = "",
                 description: str = ""):
        self.preprocessing = PreprocessingBuilder()
        self.datasource = QueryBuilder()
        self.update_func = update
        self.name = name
        self.description = description


    def _get_definition(self) -> DefinitionModel:
        '''
        _get_definition returns the definition schema of the selection

        Returns:
            DefinitionModel: the schema definition
        '''
        definition = DefinitionModel(data_selection = self.datasource.get_parameters(),
                                     preprocessing= self.preprocessing.get_params())
        definition.name = self.name
        definition.description = self.description
        return definition


    def save(self):
        '''
        save saves the selection to the backend

        '''
        definition = self._get_definition()
        self.update_func(definition)
