"""Classes to define local data selections, i.e., data elements independently from computations."""

from typing import Callable
from tuneinsight.api.sdk.models import LocalDataSelection as SelectionModel
from tuneinsight.api.sdk.models import LocalDataSelectionDefinition as DefinitionModel
from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder


class LocalDataSelection:
    """
    Combines together the data processing elements of a computation.

    A local data selection contains the datasource (especially data query) and
    preprocessing parameters.

    """

    update_func: Callable[[DefinitionModel], SelectionModel]
    preprocessing: PreprocessingBuilder = None
    datasource: QueryBuilder = None
    description: str = ""
    name: str = ""

    def __init__(
        self,
        update: Callable[[DefinitionModel], SelectionModel],
        name: str = "",
        description: str = "",
    ):
        self.preprocessing = PreprocessingBuilder()
        self.datasource = QueryBuilder()
        self.update_func = update
        self.name = name
        self.description = description

    def _get_definition(self) -> DefinitionModel:
        """
        Returns the definition schema of the selection.

        Returns:
            DefinitionModel: the schema definition
        """
        definition = DefinitionModel(
            data_selection=self.datasource.get_parameters(),
            preprocessing=self.preprocessing.get_params(),
        )
        definition.name = self.name
        definition.description = self.description
        return definition

    def save(self):
        """
        Saves the selection to the backend.

        """
        definition = self._get_definition()
        self.update_func(definition)
