"""Utilities for the generic generator.

The utilities in this module are ported from other modules (mbi and tune insight).
They are intended to allow the easy configuration of the datagen generator.

In particular, all the converters are redefined here. They allow to convert
back and forth between a data type and the MBI format. They are useful here for
 (1) computing the domain size and,
 (2) converting real data to the MBI format,
both of which are used when computing measurements on real data.

"""

import string
import datetime

from typing import Union, List

import numpy as np
import pandas as pd


# These classes are extracted from Private-PGM: https://github.com/ryan112358/private-pgm/tree/master/.


class Domain:
    def __init__(self, attrs, shape):
        """Construct a Domain object

        :param attrs: a list or tuple of attribute names
        :param shape: a list or tuple of domain sizes for each attribute
        """
        assert len(attrs) == len(shape), "dimensions must be equal"
        self.attrs = tuple(attrs)
        self.shape = tuple(shape)
        self.config = dict(zip(attrs, shape))


class Dataset:
    def __init__(self, df, domain, weights=None):
        """create a Dataset object

        :param df: a pandas dataframe
        :param domain: a domain object
        :param weight: weight for each row
        """
        assert set(domain.attrs) <= set(
            df.columns
        ), "data must contain domain attributes"
        assert weights is None or df.shape[0] == weights.size
        self.domain = domain
        self.df = df.loc[:, domain.attrs]
        self.weights = weights

    def datavector(self, flatten=True):
        """return the database in vector-of-counts form"""
        bins = [range(n + 1) for n in self.domain.shape]
        ans = np.histogramdd(self.df.values, bins, weights=self.weights)[0]
        return ans.flatten() if flatten else ans


## These classes are extracted from the Tune Insight mbi generator library.


class MBIColumnConverter:
    """Converts a column to MBI format and back."""

    def to_mbi(self, column: pd.Series) -> pd.Series:
        """Convert a column to MBI format."""
        raise NotImplementedError()

    @property
    def size(self):
        """The nnumber of entries in this attribute's domain."""
        raise NotImplementedError()


class CategoricalAttribute(MBIColumnConverter):
    """Models an attribute taking values in a known finite set."""

    def __init__(self, possible_values: List[any]):
        """
        Args
            possible_values: the list of all values that this attribute can take.
                This list needs to be exhaustive: no value can be generated outside of these,
                and values not in this list will create errors when converting to MBI.

        """
        self.possible_values = possible_values
        # Define the converters to and from the MBI format.
        self.to_ = {v: i for i, v in enumerate(possible_values)}
        self.from_ = {b: a for a, b in self.to_.items()}

    def to_mbi(self, column: pd.Series) -> pd.Series:
        return column.replace(self.to_, inplace=False)

    @property
    def size(self):
        return len(self.possible_values)


class ContinuousAttribute(MBIColumnConverter):
    """Models an attribute taking values in a known interval."""

    # Note that the conversion (esp. to_mbi) is lossy, meaning that doing
    # to_mbi -> from_mbi will not return the same values.

    def __init__(
        self,
        min_value: float,
        max_value: float,
        bins: Union[int, list] = 10,
        allow_missing: bool = False,
    ):
        """
        Args
            min_value: the smallest value that this attribute can take.
            max_value: the highest value that this attribute can take.
            bins: the edges of bins to use to discretize this attribute for MBI. If an
                integer is provided, the domain is divided into that many uniform bins.
            allow_missing: whether empty/NaN values are allowed (encoded after the last bin).

        """
        self.min_value = min_value
        self.max_value = max_value
        if isinstance(bins, int):
            self.bins = np.linspace(min_value, max_value, bins + 1)
        else:
            self.bins = bins
        self.allow_missing = allow_missing
        # The last value is where we allocate missing values.
        if self.allow_missing:
            self._missing_bin = len(self.bins)
        self.bin_size = (max_value - min_value) / self.size

    def to_mbi(self, column: pd.Series) -> pd.Series:
        if self.allow_missing:
            # Convert "" to a NaN (which is treated appropriately afterwards).
            column[column == ""] = np.nan
        # digitize returns, for each value in the column, the number of the bin
        # it is located in, starting at 0 (before any bin), and ending at num_bins+1
        # (after the last bin). We remove 1 to make 0 be the first bin.
        mbi_column = np.digitize(column, self.bins) - 1
        # Handling values outside the interval: assign to closest bin.
        mbi_column[mbi_column < 0] = 0
        mbi_column[mbi_column >= self.num_bins] = self.num_bins - 1
        if self.allow_missing:
            # Wherever there was a NaN, allocate the value to the last additional value.
            mbi_column[pd.isna(column)] = self._missing_bin
        return mbi_column

    @property
    def size(self):
        return len(self.bins) - 1

    @property
    def num_bins(self):
        return len(self.bins) - 1


class IntegerAttribute(ContinuousAttribute):
    """Models an attribute taking integer values in some range."""

    def __init__(
        self,
        min_value: int,
        max_value: int,
        bins: Union[int, list] = 10,
        allow_missing: bool = False,
    ):
        """(See ContinuousAttribute for documentation.)"""
        # Additional check: if there are less values than bins, use less bins.
        if isinstance(bins, int):
            num_values = max_value - min_value + 1
            bins = min(bins, num_values)
        ContinuousAttribute.__init__(
            self,
            min_value=min_value,
            max_value=max_value,
            bins=bins,
            allow_missing=allow_missing,
        )


class DateAttribute(IntegerAttribute):
    """Models an attribute whose values are dates, stored as strings."""

    # Internally, dates are stored as integers (number of days since start date).

    def __init__(
        self,
        start_date: str,
        end_date: str,
        bins: Union[int, list] = 10,
        strformat: str = "%Y-%m-%d",
        allow_missing: bool = False,
    ):
        """
        Args
            start_date: the minimum acceptable date (when data collection starts).
            end_date: the latest acceptable date.
            bins: either a number of bins, or specific cutoff values to use for discretisation.
            strformat: a formatting str acceptable by datetime.strptime to represent dates.
            allow_missing: whether missing values are allowed (encoded after the last bin).

        """
        self.strformat = strformat
        self.start_date = self.str_to_date(start_date)
        self.end_date = self.str_to_date(end_date)
        if self.end_date <= self.start_date:
            raise ValueError("End of period is before start.")
        gap = self.end_date - self.start_date
        # We will represents dates as integer values (# days), and convert back from it.
        # All of this will be done in to_mbi and from_mbi, with the exception of the
        # case where `bins` is a list of dates.
        if not isinstance(bins, int):
            bins = [self._date_to_days_since_start(d) for d in bins]
        IntegerAttribute.__init__(
            self,
            min_value=0,
            max_value=gap.days,
            bins=bins,
            allow_missing=allow_missing,
        )

    def _date_to_days_since_start(self, date: str) -> int:
        """Convert a date (str) to the number of days since self.start_date."""
        if self.allow_missing and date == "":
            return np.nan
        return (self.str_to_date(date) - self.start_date).days

    def to_mbi(self, column: pd.Series) -> pd.Series:
        return IntegerAttribute.to_mbi(
            self, [self._date_to_days_since_start(d) for d in column]
        )

    # Internal utilities to convert dates to and from strings.
    def str_to_date(self, date: str) -> datetime.date:
        return datetime.datetime.strptime(date, self.strformat)


class IdentifierAttribute(MBIColumnConverter):
    """Models an attribute taking unique, independent values."""

    # From a MBI perspective, such attributes are independent from everything else.
    # We implement this by having one value in the domain, and sampling from a pattern.

    PATTERN = {
        "c": list(string.ascii_lowercase),
        "C": list(string.ascii_uppercase),
        "d": list(string.digits),
        "h": list(string.hexdigits),
    }

    def __init__(self, pattern: str):
        """
        Args
            pattern: str, a pattern for the identifier. This is a string where the
                characters c, C, d, and h will be replaced by random values
                (resp. lowercase, uppercase letters, decimal, hexadecimal numbers).
                All other characters will be kept as is.

        """
        self.pattern = pattern

    def to_mbi(self, column: pd.Series):
        return np.zeros((len(column),))

    @property
    def size(self):
        return 1


class NameAttribute(IdentifierAttribute):
    """The name of a person, treated as an identifier."""

    def __init__(
        self, female_proportion=0.5, pattern="{first_name} {last_name}", locale="fr_CH"
    ):
        """
        Args
            female_proportion: fraction of the names that should be female.
            pattern (str): a format string containing {first_name} and {last_name} that
                describes how names are encoded in the data.
            locale (str): a legal Faker locale to localize the names.

        """
        IdentifierAttribute.__init__(self, pattern)
        self.female_proportion = female_proportion
        self.locale = locale
        assert 0 <= female_proportion <= 1, f"Invalid proportion: {female_proportion}."


class DatasetContext:
    """Holds all the information on a dataset to convert to and from MBI."""

    def __init__(self, names: str, converters: List[MBIColumnConverter]):
        self.names = names
        self.converters = converters
        # Generate the mbi domain object, given the domain sizes.
        self.domain = Domain(self.names, [c.size for c in self.converters])
        self.mapping = dict(zip(names, converters))

    def to_mbi(self, dataset: pd.DataFrame) -> Dataset:
        converted_columns = [
            cv.to_mbi(dataset[name]) for name, cv in zip(self.names, self.converters)
        ]
        df = pd.DataFrame(zip(*converted_columns), columns=self.names)
        return Dataset(df, self.domain)

    def __getitem__(self, column_name):
        return self.mapping[column_name]

    @classmethod
    def from_data_format(cls, data_format: List[dict]):
        """Initialize this object from the `data-format` entry of the config."""
        attribute_names = []
        converters = []
        for attribute in data_format:
            attribute_names.append(attribute.name)
            converters.append(
                available_converters[attribute.type](**attribute.parameters)
            )
        return cls(attribute_names, converters)


available_converters = {
    "categorical": CategoricalAttribute,
    "continuous": ContinuousAttribute,
    "integer": IntegerAttribute,
    "date": DateAttribute,
    "identifier": IdentifierAttribute,
    "name": NameAttribute,
}
