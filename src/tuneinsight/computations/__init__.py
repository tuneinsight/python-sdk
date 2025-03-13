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

from .base import Computation, ModelBasedComputation, KeySwitch, ComputationResult
from .count import Count, DatasetLength
from .stats import Statistics
from .aggregation import Aggregation, Sum
from .distribution import Distribution, Histogram
from .encrypted_mean import EncryptedMean
from .feasibility import Feasibility
from .gwas import GWAS
from .hybrid_fl import HybridFL
from .intersection import Matching
from .private_search import PrivateSearch
from .regression import LinearRegression, LogisticRegression, PoissonRegression
from .survival import SurvivalAnalysis, SurvivalParameters
