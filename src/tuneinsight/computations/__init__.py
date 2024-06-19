"""
# The Computations module

Defines classes to create and interact with computation on a Tune Insight instance.

The core class defined by this module is Computation, which interfaces with
the API bindings to run computations and get their results.

Specific computations are defined by the models.Computation model. This module
defines wrapper classes that allow a more user friendly interface to these
computations. The wrapper classes usually have less flexibility than modifying
the model from the API, but provide post-processing capabilities tailored to
the specific computations (e.g., plotting utilities).

This module also defines high-level classes to interface with policies, data queries,
and preprocessing (which are shared by all computations).

"""

from .base import Computation, ModelBasedComputation, KeySwitch, ComputationResult
from .count import Count, DatasetLength
from .stats import Statistics
from .aggregation import Aggregation, Sum
from .encrypted_mean import EncryptedMean
from .gwas import GWAS
from .hybrid_fl import HybridFL
from .intersection import Matching
from .private_search import PrivateSearch
from .regression import LinearRegression, LogisticRegression, PoissonRegression
from .survival import SurvivalAnalysis, SurvivalParameters
