"""Implements a wrapper for the Tune Insight Cross-Standard Feasibility Query Language (TIQL).

This wrapper can be used to define filters using a syntax similar to a `pandas.DataFrame`.

Example usage:

```python
from tuneinsight.computations import tiql

t = Dataset(datasource)
query = t.format_query(
    t.diagnostic.any(t.diagnostic.type == "E11.9") & t.treatment.all(t.treatment.code != "ATC-123")
)
comp.datasource.set_cross_standard_query(query)
```

Alternatively, to avoid repetition of `t.`, the following lambda syntax is supported:

```
query = t.format.query(
    t.diagnostic.any(
        lambda diag: diag.type == "E11.9")
    ) & t.treatment.all(
        lambda treatment: treatment.code != "ATC-123"
    )
)
```
"""

from typing import Any, Callable, Optional, TypeAlias, Union
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET

from tuneinsight.client import DataSource


def AND(filters: list[models.AdvancedFilter]):
    """Creates a disjunctive filter from a list of sub-filters."""
    return models.LogicalOperatorFilter(
        type=models.AdvancedFilterType.LOGICALOPERATORFILTER,
        operator=models.LogicalOperator.AND,
        filters=filters,
    )


def OR(filters: list[models.AdvancedFilter]):
    """Creates a conjunctive filter from a list of sub-filters."""
    return models.LogicalOperatorFilter(
        type=models.AdvancedFilterType.LOGICALOPERATORFILTER,
        operator=models.LogicalOperator.OR,
        filters=filters,
    )


class _WrappedFilter:
    """A wrapper class over AdvancedFilter that supports AND and OR operations."""

    def __init__(self, filter_: models.AdvancedFilter):
        self.filter = filter_
        self.simplify()

    def __and__(self, other: "_WrappedFilter"):
        return _WrappedFilter(AND([self.unwrap(), other.unwrap()]))

    def __or__(self, other: "_WrappedFilter"):
        return _WrappedFilter(OR([self.unwrap(), other.unwrap()]))

    def simplify(self):
        """Simplifies groups together in case of nested ANDs or ORs."""
        if isinstance(self.filter, models.LogicalOperatorFilter):
            operator = self.filter.operator
            # Go through the filter tree, grouping together all logical operators with the same operator.
            leaves = []
            sub_filters = list(self.filter.filters)
            while len(sub_filters) > 0:
                f = sub_filters.pop(0)  # Remove the first entry to keep in order.
                if (
                    isinstance(f, models.LogicalOperatorFilter)
                    and f.operator == operator
                ):
                    sub_filters += f.filters
                else:
                    leaves.append(f)
            self.filter.filters = leaves

    def unwrap(self) -> models.AdvancedFilter:
        return self.filter


class _ComparableValue:
    """
    A value in the TIQL namespace that can be compared to other values.

    This includes fields of a concept and variables defined in the namespace.
    This class implements all common elements and is meant to be subclassed.
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, value):
        return self._cmp(value, models.ComparisonType.EQUAL)

    def __ne__(self, value):
        return self._cmp(value, models.ComparisonType.NEQUAL)

    def __ge__(self, value):
        return self._cmp(value, models.ComparisonType.GREATEREQ)

    def __gt__(self, value):
        return self._cmp(value, models.ComparisonType.GREATER)

    def __le__(self, value):
        return self._cmp(value, models.ComparisonType.LESSEQ)

    def __lt__(self, value):
        return self._cmp(value, models.ComparisonType.LESS)

    def _cmp(self, value: Any, comparator: models.ComparisonType):
        """Returns a wrapped atomic filter for the comparison between this value and another."""
        # Check that this object supports comparison with the given value.
        self._assert_can_compare(value)
        # TIQL supports comparison with static values and variables identified by their name.
        rh_value = UNSET
        rh_variable = UNSET
        if isinstance(value, _ComparableValue):
            rh_variable = value.name
        else:
            rh_value = str(value)
        filter_ = models.AtomicFilter(
            type=models.AdvancedFilterType.ATOMICFILTER,
            comparator=comparator,
            left_hand_variable=self.name,
            right_hand_value=rh_value,
            right_hand_variable=rh_variable,
        )
        return _WrappedFilter(filter_)

    # pylint: disable=unused-argument
    def _assert_can_compare(self, other: Union["_ComparableValue", Any]):
        """Asserts that comparison is allowed between this value and another one."""
        # By default, all is allowed: subclasses should override this.
        return


class _Field(_ComparableValue):
    """Internal class representing a TIQL field on a concept."""

    def __init__(self, concept: "_Concept", field: models.TiqlField):
        self._concept = concept
        self._field = field
        super().__init__(field.name)

    @property
    def type(self) -> str:
        """The type of the values that this field takes."""
        return self._field.type

    @property
    def concept(self) -> "_Concept":
        """The concept that this field is defined on."""
        return self._concept

    def _assert_can_compare(self, other: Union["_ComparableValue", Any]):
        """Fields can be compared with anything, except fields from other concepts."""
        if not isinstance(other, _Field):
            return
        # For fields, comparison is currently only allowed within the same concept.
        assert (
            self.concept.name == other.concept.name
        ), "comparisons are only allowed between fields of the same concept"


class OutputVariable(_ComparableValue):
    """
    An output variable in a concept filter.

    To output a variable from a concept filter, add it to the `outputs` argument
    of `filter.any` or `filter.all`. This variable can then also be used as a
    right-hand operand in comparison with fields in the data.
    """

    def __init__(self, field: "_Field", variable_name: str = None):
        """
        Args:
            field (_Field): the field from which the variable is extracted.
            variable_name (str, optional): the unique name to refer to this variable. If not provided,
                field.name is used instead (which is not recommended, as it can create conflicts).
        """
        self.field = field
        self.variable_name = variable_name or field.name
        super().__init__(self.variable_name)

    def to_model(self) -> models.SeriesFilterOutputVariablesItem:
        """Converts this object to a variable definition to use in a series filter."""
        return models.SeriesFilterOutputVariablesItem(
            name=self.variable_name,
            source=self.field.name,
            entry_selection_criterion=models.TiqlSelectionCriterion.FIRST,
        )

    def to_query_output_variable(self) -> models.QueryOutputVariable:
        """Converts this variable to an output variable definition to set at the top-level of the query."""
        return models.QueryOutputVariable(
            name=self.variable_name,
            series=self.field.concept,
        )

    def _assert_can_compare(self, other: Union["_ComparableValue", Any]):
        raise SyntaxError("variable cannot be compared as a left-hand operand")

    def is_same(self, other: "OutputVariable"):
        """Returns whether two variables are the same. Use instead of == since __eq__ is overriden."""
        if type(self) != type(other):
            return False
        return (
            self.variable_name == other.variable_name
            and self.field.concept == other.field.concept
            and self.field.name == other.field.name
        )


class OutputCount(OutputVariable):
    """
    A variable obtained by counting the number of entries matching a concept filter.

    Note: this variable can be instantiated "alone", but needs to be attached to a filter
    to become meaningful. For this, add it to the `outputs` argument of `filter.any` or
    `filter.all`. Like other variables, it can then also be used as a right-hand operand
    in comparison with fields in the data.

    """

    def __init__(self, variable_name: str):
        """
        Args:
            variable_name (str): the name of this variable.
        """
        super().__init__(None, variable_name)

    def to_model(self):
        raise TypeError("Variables issued from a count cannot be defined by a model.")

    def to_query_output_variable(self) -> models.QueryOutputVariable:
        """Converts this variable to an output variable definition to set at the top-level of the query."""
        return models.QueryOutputVariable(
            name=self.variable_name,
        )

    def is_same(self, other):
        if not isinstance(other, OutputCount):
            return False
        return self.name == other.name


ConceptFilter: TypeAlias = _WrappedFilter | Callable[["_Concept"], _WrappedFilter]
"""
A ConceptFilter describes concepts over filters. These can either be a models.AdvancedFilter
that is constituted as ANDs and ORs over SeriesFilter, typically constructed directly
as a logical expression with concept.field, or as a callable of the concept that returns such an
expression. This latter form allows for some lighter syntax, of the form:
    lambda diagnostic: (diagnostic.type == "ABC") & (diagnostic.date >= "01/01/2000")
instead of the more cumbersome
    (t.diagnostic.type == "ABC") & (t.diagnostic.date >= "01/01/2000")
Both are strictly equivalent:  the second form is obtained immediately by calling the
first with argument t.diagnostic.
"""


class _Concept:
    """Internal class representing a TIQL concept (aka series) with subfields."""

    def __init__(self, dataset: "Dataset", model: models.TiqlConcept):
        self._dataset = dataset
        self._model = model
        self._name = model.name
        self._fields = {}
        for field in model.fields:
            f = _Field(self, field)
            setattr(self, field.name, f)
            self._fields[field.name] = f

    @property
    def name(self) -> str:
        """Unique name of this concept in the data."""
        return self._name

    def all(
        self,
        filter_: ConceptFilter,
        outputs: list[OutputVariable] = None,
    ) -> _WrappedFilter:
        """Requires that the inner filter is satisfied by all entries in the data."""
        return self._series_filter(filter_, models.BooleanAggregator.ALL, outputs)

    def any(
        self,
        filter_: ConceptFilter,
        outputs: list[OutputVariable] = None,
    ) -> _WrappedFilter:
        """Requires that the inner filter is satisfied by any entry in the data."""
        return self._series_filter(filter_, models.BooleanAggregator.ANY, outputs)

    def _series_filter(
        self,
        filter_: ConceptFilter,
        aggregator: models.BooleanAggregator,
        outputs: list[OutputVariable] = None,
    ) -> _WrappedFilter:
        if not isinstance(filter_, _WrappedFilter):
            # This is a callable that expects a Concept as input.
            filter_ = filter_(self)
        elif not callable(filter_):
            raise ValueError(
                f"Invalid type for input filter {type(filter_)}: {filter_}."
            )
        # Validate that the input filter applies to this filter.
        self._assert_filter_validity(filter_.unwrap())
        # Save all the variables in the "Dataset".
        output_variable_models = UNSET
        output_count_as_variable = UNSET
        if outputs is not None:
            output_variable_models = []
            for o in outputs:
                if isinstance(o, OutputCount):
                    output_count_as_variable = o.name
                elif isinstance(o, OutputVariable):
                    output_variable_models.append(o.to_model())
                else:
                    raise TypeError(f"Invalid type for output: {type(o)}")
            # Add the variables to the namespace.
            for variable in outputs:
                self._dataset.variables.add(variable)
        # Return the corresponding series filter, wrapped to allow comparisons.
        return _WrappedFilter(
            models.SeriesFilter(
                type=models.AdvancedFilterType.SERIESFILTER,
                filter_=filter_.unwrap(),
                logical_aggregator=aggregator,
                series=self._name,
                output_variables=output_variable_models,
                output_count_as_variable=output_count_as_variable,
            )
        )

    def _assert_filter_validity(self, filter_: models.AdvancedFilter):
        """Checks that the internal filter concerns this concept and does not include a Series."""
        if isinstance(filter_, models.SeriesFilter):
            raise ValueError("SeriesFilters cannot be nested")
        if isinstance(filter_, models.LogicalOperatorFilter):
            for f in filter_.filters:
                self._assert_filter_validity(f)
        if isinstance(filter_, models.AtomicFilter):
            assert (
                filter_.left_hand_variable in self._fields
            ), f"field {filter_.left_hand_variable} not found on concept {self.name}"

    def __getitem__(self, field_name: str) -> _Field:
        return self._fields[field_name]


class _VariableStore:
    """
    Class representing the TIQL namespace, storing all variables defined within the query.

    Specifically, this store contains all variables defined in concept filters, which
    are represented by `OutputVariable` objects. Note that variables do not have a value
    assigned until the query is executed in the backend.

    Variables in the store can be accessed with __getitem__ notation store[varname],
    or directly as an attribute of this instantiated object, store.varname.

    This class should not be instantiated directly. Instead, use `Dataset.variables`
    to interact with the variables defined for a query.
    """

    def __init__(self):
        self.variables = {}

    def add(self, variable: OutputVariable):
        """Adds a variable to the store."""
        if variable.name in self.variables:
            raise NameError(f"two variables with the same name: {variable.name}")
        self.variables[variable.name] = variable
        setattr(self, variable.name, variable)

    def __getitem__(self, name):
        return self.variables[name]

    def __iter__(self):
        return iter(self.variables.values())

    def find(self, variable: str | OutputVariable):
        """Attempts to find a variable in the store.

        This is used to validate that a variable is defined before being returned.

        Args:
            variable (str | OutputVariable): either the name of the variable, or the
                object of that variable (which must match exactly).
        """
        if isinstance(variable, str):
            return self.variables[variable]
        if not isinstance(variable, OutputVariable):
            raise TypeError(f"Invalid type for variable: {type(variable)}")
        # Check that a variable with this name exists in the store.
        if variable.name not in self.variables:
            raise NameError(f"Variable named {variable.name} not found in query.")
        found_variable = self.variables[variable.name]
        if not variable.is_same(found_variable):
            raise ValueError("mismatching variables with the same name!")
        return found_variable

    def reset(self):
        """Removes all variables currently in the store."""
        self.variables = {}


class Dataset:
    """
    A TIQL dataset with variables and fields.

    This abstraction is used to define TIQL queries on a datasource in a Pythonic way.
    The name of fields is set as a field on this object, if possible.

    """

    def __init__(self, datasource: DataSource):
        self._ds = datasource
        self.variables = _VariableStore()
        self._init_from_commands()

    def _init_from_commands(self):
        """Sets up the correct variables and fields based on the results from datasource commands."""
        res: models.GetMetadataCommandResult = self._ds.execute_command(
            models.DataSourceCommand(
                type=models.DataSourceCommandType.GETMETADATACOMMAND
            )
        )
        self.concepts = {}
        for concept in res.concepts:
            c = self._init_concept(concept)
            self.concepts[concept.name] = c

    def _init_concept(self, concept: models.TiqlConcept) -> _Concept:
        """Internally sets up a concept on this datasource."""
        concept = _Concept(self, concept)
        # Set the named attribute of this concept
        setattr(self, concept.name, concept)
        return concept

    def __getitem__(self, concept_name):
        return self.concepts[concept_name]

    def get_query(
        self,
        filter_: _WrappedFilter,
        variables: Optional[list[str | OutputVariable]] = None,
    ) -> models.CrossStandardQuery:
        """Formats the query object defined with this object to a cross-standard query.

        Args:
            filter_ (_WrappedFilter): the main filter of this query (containing all nested
                sub-filters). This is obtained with the syntax sugar on `Dataset`.
            variables (list[str | OutputVariable], Optional): the variables to return for
                records that pass the filters. All variables named here must be defined by
                the query. If None, all variables defined in the query are returned.

        Returns:
            models.CrossStandardQuery: the formatted TIQL query.
        """
        # Select all variables to extract.
        variables_to_extract = self.variables
        if variables is not None:
            variables_to_extract = [self.variables.find(v) for v in variables]
        # Format the API model for these variables.
        variables = [v.name for v in variables_to_extract]
        output_variables = [v.to_query_output_variable() for v in variables_to_extract]
        return models.CrossStandardQuery(
            filter_=filter_.unwrap(),
            variables=variables,
            output_variables=output_variables,
        )
