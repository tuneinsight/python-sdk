"""Implements a wrapper for the Tune Insight Cross-Standard Feasibility Query Language (TIQL)."""

from typing import Any, List, Union
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import UNSET


def AND(filters: List[models.AdvancedFilter]):
    """Creates a disjunctive filter from a list of sub-filters."""
    return models.LogicalOperatorFilter(
        type=models.AdvancedFilterType.LOGICALOPERATORFILTER,
        operator=models.LogicalOperator.AND,
        filters=filters,
    )


def OR(filters: List[models.AdvancedFilter]):
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
        return _WrappedFilter(AND([self.filter, other.filter]))

    def __or__(self, other: "_WrappedFilter"):
        return _WrappedFilter(OR([self.filter, other.filter]))

    def simplify(self):
        """Simplifies groups together nested ANDs or ORs."""
        if isinstance(self.filter, models.LogicalOperatorFilter):
            operator = self.filter.operator
            # Go through the filter tree, grouping together all logical operators with the same operator.
            leaves = []
            sub_filters = list(self.filter.filters)
            while len(sub_filters) > 0:
                f = sub_filters.pop()
                if (
                    isinstance(f, models.LogicalOperatorFilter)
                    and f.operator == operator
                ):
                    sub_filters += f.filters
                else:
                    leaves.append(f)
            self.filter.filters = leaves


class Variable:
    """An abstraction to create filters using arithmetic operations."""

    def __init__(self, name):
        self.name = name

    def __eq__(self, value):
        return self._cmp(value, models.ComparisonType.EQUAL)

    def __neq__(self, value):
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
        """Returns a wrapped atomic filter"""
        rh_value = UNSET
        rh_variable = UNSET
        if isinstance(value, Variable):
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


class _VariableBuilder:

    def __getattribute__(self, name):
        return Variable(name)

    def __getitem__(self, key):
        return Variable(str(key))


class Builder:
    """Syntax sugar class to build a Cross-Standard Feasibility query."""

    def __init__(self, variables: List[str]):
        """
        Args:
            variables (List[str]): the variables to extract from the query
        """
        self.model = models.CrossStandardQuery(
            variables=variables,
        )

    def set_filter(self, filter_: Union[_WrappedFilter, models.AdvancedFilter]):
        if isinstance(filter_, _WrappedFilter):
            filter_ = filter_.filter
        self.model.filter_ = filter_

    def get_model(self) -> models.CrossStandardQuery:
        """Returns the API model for the cross-standard query."""
        return self.model

    @property
    def df(self):
        return _VariableBuilder()
