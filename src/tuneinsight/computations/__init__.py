"""
# Running computations

This module defines classes to create and run computations on a Tune Insight instance,
as well as get and analyze the results from computations.

## The `Computation` architecture

The core class defined by this module is `Computation`, which interfaces with
the API bindings to run computations and get their results. All computations are
created and parameterized via their constructor method:

```python
    computation = ComputationClass(project, **additional_parameters)
```

This also sets the computation on the `project`, and broadcasts it to all other
project participants. Running a computation on the project is done with the `.run`
method (and its key parameter `local`):

```python
    result = computation.run(local=False)
```

Specific computations inherit from the base `Computation` class, and provide high-level
pre-processing of arguments, high-level post-processing of results, and additional methods
to visualize results.

This module also defines high-level classes to interface with policies, data queries,
and preprocessing (which are shared by all computations).

## Documentation page

https://dev.tuneinsight.com/docs/Usage/python-sdk/computations/

## Importing computations

All computation classes are available from the `tuneinsight.computations` module directly.
For instance, to create an `Aggregation` computation, use

```python
from tuneinsight.computations import Aggregation
```
"""

from importlib.util import find_spec
from typing import Any, NoReturn

from .aggregation import Aggregation, Sum
from .base import Computation, ComputationResult, KeySwitch, ModelBasedComputation
from .count import Count, DatasetLength
from .distribution import Distribution, Histogram
from .encrypted_mean import EncryptedMean
from .feasibility import Feasibility
from .filtered_aggregation import FilteredAggregation
from .heatmap import HeatMap
from .intersection import Matching
from .regression import LinearRegression, LogisticRegression, PoissonRegression
from .stats import Statistics
from .survival import SurvivalAnalysis, SurvivalParameters

# HybridFL depends on the optional ti-models package, which is not part of the base SDK install.
HybridFL: type[ModelBasedComputation]

try:
    from .hybrid_fl import HybridFL as _ImportedHybridFL
except ModuleNotFoundError as exc:
    if find_spec("ti_models") is not None:
        raise

    _hybridfl_import_error = exc

    def _raise_hybridfl_import_error() -> NoReturn:
        raise ModuleNotFoundError(
            "HybridFL requires the optional 'ti-models' dependency. "
            "Install tuneinsight[ml] to use it."
        ) from _hybridfl_import_error

    class _MissingHybridFL(ModelBasedComputation):
        def __init__(self, *_args: Any, **_kwargs: Any) -> None:
            _raise_hybridfl_import_error()

        @classmethod
        def from_model(cls, *_args: Any, **_kwargs: Any) -> "_MissingHybridFL":
            _raise_hybridfl_import_error()

    HybridFL = _MissingHybridFL
else:
    HybridFL = _ImportedHybridFL
