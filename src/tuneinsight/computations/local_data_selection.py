"""Classes to define local data selections, i.e., data elements independently from computations."""

from typing import Optional

from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import is_set

from tuneinsight.computations.queries import QueryBuilder
from tuneinsight.computations.preprocessing import PreprocessingBuilder


class LocalDataSelection:
    """
    Combines together the data processing elements of a computation: data query and preprocessing.

    From version 0.13.0 onwards, the local data selection abstraction only exists on the client
    side (i.e., it is no longer part of the project definition hosted on the server). This
    object maintains the same behavior as before: it is initialized based on the parameters of
    the computation definition available in the project.

    """

    preprocessing: PreprocessingBuilder = None
    datasource: QueryBuilder = None

    def __init__(
        self,
        compdef: Optional[models.ComputationDefinition] = None,
    ):
        """Initializes this local data selection object.

        Args:
            compdef (Optional[models.ComputationDefinition], optional): an optional computation definition
                from which to extract the preprocessing and datasource parameters. Defaults to None.
        """
        self.preprocessing = PreprocessingBuilder(lambda: "")  # Disable warning.
        self.datasource = QueryBuilder()
        if compdef is not None and is_set(compdef):
            if is_set(compdef.preprocessing_parameters):
                self.preprocessing.from_model(compdef.preprocessing_parameters)
            if is_set(compdef.data_source_parameters):
                self.datasource.set_model(compdef.data_source_parameters)

    def to_model(self) -> models.LocalDataSelectionDefinition:
        """
        Returns the definition schema of the selection.

        Returns:
            DefinitionModel: the schema definition
        """
        definition = models.LocalDataSelectionDefinition(
            data_selection=self.datasource.get_model(),
            preprocessing=self.preprocessing.get_model(),
        )
        return definition
