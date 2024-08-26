"""Classes interacting with policies on a project."""

from typing import List, Union

import json
import datetime

from tuneinsight.computations.preprocessing import Operation
from tuneinsight.computations.types import Type, displayed_types
from tuneinsight.utils.display import Renderer
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Unset


class Policy(models.ComputationPolicy):
    """
    Policy related to a computation.

    A policy defines a set of constraints and disclosure prevention mechanisms
    that are applied to a project in order to limit what users can do and the
    amount of personal information leakage.

    """

    @classmethod
    def from_model(cls, policy: models.ComputationPolicy):
        """
        Initializes a policy object given a computation policy

        Args:
            policy (models.ComputationPolicy): the policy API model

        Returns:
            Policy: the policy object.
        """
        p = cls()
        for attr_name, attr_value in policy.__dict__.items():
            if not isinstance(attr_value, Unset) and attr_value is not None:
                setattr(p, attr_name, attr_value)
        return p

    def __init__(self):
        super().__init__()
        self.authorized_preprocessing_operations = []
        self.authorized_data_source_queries = []
        self.fixed_parameters = []
        self.flexible_parameters = []
        self.dp_policy = models.DPPolicy()

    def add_authorized_preprocessing(
        self, operations: Union[List[Operation], "PreprocessingBuilder"]  # type: ignore
    ):
        """
        Authorizes a preprocessing operation.

        Appends "operations" to the set of authorized preprocessing operation types.
        By default, all operations are authorized: using this function automatically
        unauthorizes all operations that are not explicitly authorized.

        Args:
            operations: either a list of preprocessing.Operation, or the preprocessing builder instance.
        """
        auth_operations = set(self.authorized_preprocessing_operations)
        for op in operations:
            auth_operations.add(
                models.PreprocessingOperationType(op.to_preproc_operation_type())
            )
        self.authorized_preprocessing_operations = list(auth_operations)

    def add_authorized_query(self, query: str, name: str = ""):
        """
        Adds a datasource query to the set of authorized queries.

        By default, all queries are authorized: using this function automatically
        unauthorizes all queries that are not explicitly authorized.

        Args:
            query (str): the data source query string
        """
        if self.authorized_data_source_queries is Unset:
            self.authorized_data_source_queries = []
        self.authorized_data_source_queries.append(
            models.WhitelistedQuery(name=name, raw_query=query)
        )

    def set_column_restrictions(self, restricted: bool = True):
        """
        Controls whether the input dataset columns must be restricted to the set of authorized columns
        that have been added to this policy

        Args:
            restricted (bool, optional): Whether to restrict columns or not. Defaults to True.
        """
        self.dp_policy.restrict_columns = restricted

    def add_authorized_column(
        self,
        column: str,
        categorical: bool = False,
        max_categories: Union[int, float] = 0,
    ):
        """
        adds a column to the set of authorized columns in the dataset.

        Args:
            column (str): the column to authorize querying on.
            categorical (bool, optional): whether the column should always be treated as a categorical column. Defaults to False.
            max_categories (int | float, optional): when the column is categorical, maximum amount of categories that it can take. Defaults to 0.
                This value can also be set as a factor of the dataset size between 0 and 1.
        """
        col = models.AuthorizedColumn(name=column, categorical=categorical)
        if max_categories > 0:
            if max_categories < 1:
                col.max_categories = models.Threshold(
                    relative_factor=max_categories, type=models.ThresholdType.RELATIVE
                )
            else:
                col.max_categories = models.Threshold(
                    fixed_value=max_categories, type=models.ThresholdType.FIXED
                )
        if self.dp_policy.authorized_columns is Unset:
            self.dp_policy.authorized_columns = []
        self.dp_policy.authorized_columns.append(col)

    @staticmethod
    def __new_threshold(
        relative: bool = False, fixed_value: int = 10, relative_factor: float = 0.2
    ) -> models.Threshold:
        if relative:
            threshold_type = models.ThresholdType.RELATIVE
        else:
            threshold_type = models.ThresholdType.FIXED
        return models.Threshold(
            fixed_value=fixed_value,
            relative_factor=relative_factor,
            type=threshold_type,
        )

    def enable_differential_privacy(self):
        """
        Enables the use of differential privacy (DP) in this project.

        When using DP, additional randomness is added to the outputs of a project
        in order to protect the privacy of data subjects. Only a subset of operations
        are allowed when using differential privacy. Each computation exhausts a
        fraction of the execution quota (called privacy budget).

        See the documentation for more details.

        """
        self.dp_policy.use_differential_privacy = True

    def disable_differential_privacy(self):
        """
        Disables the use of differential privacy (DP) in this project.

        """
        self.dp_policy.use_differential_privacy = False

    def set_max_columns(
        self, relative: bool = False, fixed_value: int = 5, relative_factor: float = 0.2
    ):
        """
        Sets the maximum number of columns that can be input to the computation.

        Args:
            relative (bool, optional): whether or not the maximum value is relative to the dataset size. Defaults to False.
            fixed_value (int, optional): absolute maximum value when not relative. Defaults to 5.
            relative_factor (float, optional): factor of the dataset size when relative. Defaults to 0.2.
        """
        self.dp_policy.max_column_count = self.__new_threshold(
            relative, fixed_value, relative_factor
        )

    def set_quota(
        self,
        initial: int,
        reallocation_amount: int = 0,
        reallocation_interval_hours: int = 24,
        max_quota: int = None,
    ):
        """
        Defines a quota for limiting the workflow executions in the project.

        By default, The quota is defined in terms of number of queries. Executing any distributed or
        collective workflow exhausts some computation quota. Once the quota is exhausted, no (collective)
        computation can be run until the quota is refreshed.

        When using Differential Privacy, this is the total privacy budget that can be used in the project.

        When running encrypted matching or set intersection workflows, the query cost is equal to the number
        of matching queries / set size.

        The quota is defined by specifying an initial amount allocated globally for the project, along with
        an optional reallocation amount and interval.

        Args:
            initial (int): corresponds to the initial quota allocated to the project.
            reallocation_amount (int, optional): the amount reallocated at every
                reallocation interval. Defaults to 0.
            reallocation_interval_hours (int, optional): the interval in terms of hours
                at which the quota is reallocated. Defaults to 24.
            max_quota (int, optional): the absolute limit to the quota. If not specified
                it will be set to the initial allocated amount. Defaults to None.
        """
        if max_quota is None:
            max_quota = initial
        start_time = datetime.datetime.now(datetime.timezone.utc)
        interval = models.Duration(
            unit=models.TimeUnit.HOURS, value=reallocation_interval_hours
        )
        self.dp_policy.execution_quota_parameters = models.ExecutionQuotaParameters(
            allocation=initial,
            increment=reallocation_amount,
            max_allocation=max_quota,
            scope=models.ExecutionQuotaParametersScope.PROJECT,
            start=start_time,
            allocation_interval=interval,
        )

    def add_authorized_computation_type(self, computation_type: Type):
        """
        Adds a computation type to the list of whitelisted computation types. If no computations type were set before,
        then the policy restricts running only the provided computation type.

        Args:
            computation_type (Type): the type of computation / workflow to whitelist.
        """
        if isinstance(self.authorized_computation_types, Unset):
            self.authorized_computation_types = []
        comp_types = set(self.authorized_computation_types)
        comp_types.add(models.ComputationType(computation_type.to_computation_type()))
        self.authorized_computation_types = list(comp_types)

    def set_contract(
        self,
        computation_type=False,
        computation_parameters=False,
        preprocessing=False,
        data_query=False,
    ):
        """
        Sets the authorization contract of the project.

        Once a project is authorized by at least one participant, the authorization contract
        defines what parts of the project can still be modified by participants. Hence, all
        runs of the project will have the exact same locked parts, but can potentially differ
        in non-locked parts (as well as changes in the underlying data).

        The parameters of this function are the different parts of a project that can opened
        up under an authorization contract. Setting True to a parameters opens it up for
        modification. The default is False (restrictive).

        Parameters:
            computation_type: whether the computation type of the project can change.
            computation_parameters: whether computation parameters can change.
            preprocessing: whether the preprocessing chain can change.
            data_query: whether the query performed on the data can change.
        """
        if computation_type and not computation_parameters:
            raise ValueError("Inconsistent contract")
        self.authorization_contract = models.AuthorizationContract(
            computation_type=computation_type,
            computation_parameters=computation_type,
            preprocessing=preprocessing,
            data_query=data_query,
        )

    def set_min_dataset_size(self, local_size: int = None, collective_size: int = None):
        """
        Sets a minimum dataset size policy either on the local (per-instance) datasets or the collective (including all participants) dataset.

        Args:
            local_size (int, optional): minimum dataset size that should be satisfied from all participating organizations locally. Defaults to None.
            collective_size (int, optional): minimum dataset size that should be satisfied from the collective dataset of all organizations. Defaults to None.

        Raises:
            ValueError: if both the local and collective size arguments have not been provided to this method.
        """
        if local_size is None and collective_size is None:
            raise ValueError(
                "No dataset size was provided (at least one of local_size or collective_size must be set)."
            )
        if local_size is not None:
            self.dp_policy.min_dataset_size = int(local_size)
        if collective_size is not None:
            self.dp_policy.min_global_dataset_size = int(collective_size)


displayed_labels = {
    "validateParameters": "template validation",
    "fixedParameters": "fixed",
    "flexibleParameters": "flexible",
    "restrictDataSourceQueries": "validate queries",
    "authorizedDataSourceQueries": "authorized queries",
    "restrictPreprocessingOperations": "validate operations",
    "authorizedPreprocessingOperations": "authorized operations",
    "consideredVariables": "authorized variables",
    "minDatasetSize": "min rows",
    "minFrequencies": "min frequencies",
    "maxColumnCount": "max columns",
}


# pylint: disable=R0912
# (disabled because this function simply displays some markdown and has to check for each field if set)
def display_policy(
    p: models.ComputationPolicy, detailed: bool = False, show_queries: bool = True
):
    """
    Displays a user-friendly summary of project policies in markdown format.

    Args:
        p (models.ComputationPolicy): the policy do display.
        detailed (bool, optional): whether or not to display the detailed json version of the policy. Defaults to False.
        show_queries (bool, optional): whether to display the list of restricted data source queries. Defaults to True.
    """
    r = Renderer()
    if (
        p.restrict_data_source_queries
        or p.restrict_preprocessing_operations
        or not isinstance(p.authorized_computation_types, Unset)
    ):
        r.h3("Workflow Restrictions")
        r(
            "These restriction limit the data source queries, preprocessing operations and distributed workflows that can run in this project."
        )
    if p.restrict_preprocessing_operations:
        if len(p.authorized_preprocessing_operations) > 0:
            r(
                "The policy only allows the following preprocessing operations to be used:"
            )
            for op in p.authorized_preprocessing_operations:
                r(f"- {op.value}")
        else:
            r("The policy forbids the use of any preprocessing operation.")
    if p.restrict_data_source_queries:
        if show_queries:
            r("The policy restricts data source queries to the following set:")
            for q in p.authorized_data_source_queries:
                r(f"- `{q}`")
        else:
            r("- The policy allows only specific data source queries (not shown here).")
    if (
        not isinstance(p.authorized_computation_types, Unset)
        and len(p.authorized_computation_types) > 0
    ):
        r(
            "The policy forbids running any computation type that is not one of the following:"
        )
        for comp in p.authorized_computation_types:
            comp_type = Type(comp)
            displayed_type = comp.value
            if comp_type in displayed_types:
                displayed_type = displayed_types[Type(comp)]
            r(f"- {displayed_type}")
    else:
        r("The policy allow running any computation type.")
    if not isinstance(p.dp_policy, Unset):
        dp = p.dp_policy
        display_dp_policy(dp)
    if detailed:
        r.h3("Detailed Policy (JSON)")
        dict_values = p.to_dict()
        dict_values.pop("authorizedDataSourceQueries")
        json_formatted_str = json.dumps(dict_values, indent=2)
        r(r.code_block(json_formatted_str, lang="json"))


def display_threshold(r: Renderer, text: str, t: models.Threshold):
    """Displays a user-friendly description of a thresholding policy using IPython.display."""
    if t.type == models.ThresholdType.FIXED:
        r(text + ":", r.math(t.fixed_value))
    else:
        r(
            text + ":",
            r.math(f"{t.relative_factor} N"),
            "(where",
            r.math("N"),
            "is the local dataset size",
        )


# pylint: disable=R0915
# (disabled because this function is responsible for generating markdown for many parameters, refactoring it does not make things neater)
def display_dp_policy(dp: models.DPPolicy, r: Renderer = None):
    """Displays a user-friendly description of a DP policy using IPython.display."""
    if r is None:
        r = Renderer()
    if isinstance(dp.authorized_columns, list) and len(dp.authorized_columns) > 0:
        r.h4("Dataset column validation")
        r(
            "This check ensures that the input dataset only contains a set of authorized columns."
        )
        r(
            "Any column that is not in the following set",
            r.code([column.name for column in dp.authorized_columns]),
            "is automatically dropped from the input dataset.",
        )
    if not isinstance(dp.min_dataset_size, Unset):
        r.h3("Local dataset minimum size validation")
        r(
            "The dataset must contain at least",
            r.code(dp.min_dataset_size),
            "or the computation will be aborted.",
        )
    if not isinstance(dp.min_global_dataset_size, Unset):
        r.h3("Collective dataset minimum size validation")
        r(
            "The collective dataset must contain at least",
            r.code(dp.min_global_dataset_size),
            "or the computation will be aborted.",
        )
        r.it(
            "The collective dataset size is computed under encryption and then decrypted by all participants."
        )
    if not isinstance(dp.max_column_count, Unset):
        r.h3("Maximum Number of Columns")
        display_threshold(r, "Threshold", dp.max_column_count)
        r(
            "this limits the number of columns which can be created during the preprocessing, avoiding that a subsequent aggregation leaks individual information."
        )

    use_dp = (
        not isinstance(dp.use_differential_privacy, Unset)
        and dp.use_differential_privacy
    )
    if use_dp:
        r.h3("This project uses differential privacy.")
        r(
            "Only computations that support differential privacy can be run on this project.",
            "Each computation will use some of the budget.",
        )
    if not isinstance(dp.execution_quota_parameters, Unset):
        bp = dp.execution_quota_parameters
        r.h4("Query Limiting parameters")
        alloc_start = bp.start.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        scope = bp.scope
        if scope == "":
            scope = "project"
        allocated = bp.allocation
        if isinstance(allocated, Unset):
            allocated = 0

        quota = "budget $\\varepsilon$" if use_dp else "quota"
        r(
            f"Query limits are enforced in this project through a {quota} that is allocated at the {scope} level.",
        )
        if use_dp:
            r(
                "Each distributed workflow run on this project consumes some user-defined amount of the budget."
            )
        else:
            r(
                f"Quotas represent the maximum amount of distributed workflows that can be run for each {scope}.",
            )
        r(
            f"- A {quota} of {allocated} is initially allocated at the following date `{alloc_start}`."
        )

        if (
            not isinstance(bp.increment, Unset)
            and bp.increment > 0
            and not isinstance(bp.allocation_interval, Unset)
        ):
            r(
                f"- The {quota} is reallocated by {bp.increment} queries each {bp.allocation_interval.value} {bp.allocation_interval.unit} and cannot exceed {bp.max_allocation}."
            )

        if not use_dp:
            r(
                "*Note that, depending on the specific workflow, the cost of a single workflow can exceed 1 in terms of quota.*"
            )
