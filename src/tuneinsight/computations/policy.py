import json
from typing import List
from IPython.display import display, Markdown
from tuneinsight.computations.types import Type
from tuneinsight.computations.preprocessing import Operation
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import Unset



class Policy(models.ComputationPolicy):
    '''
    Policy related to a computation. Defines a set of constraints and Disclosure Prevention Mechanisms

    Args:
        models (_type_): _description_
    '''

    computation_type: models.ComputationType

    def __init__(self,computation_type: Type):
        '''
        __init__ initializes the the policy using the computation type

        Args:
            computation_type (Type): _description_
        '''
        super().__init__()
        self.authorized_preprocessing_operations = []
        self.authorized_data_source_queries = []
        self.fixed_parameters = []
        self.flexible_parameters = []
        self.dp_policy = models.DPPolicy()
        self.computation_type = computation_type.to_computation_type()


    def add_authorized_preprocessing(self,operations: List[Operation]):
        '''
        add_authorized_preprocessing appends the set of operations from the preprocessing builder instance
        to the set of authorized preprocessing operation types

        Args:
            operations (PreprocessingBuilder): the preprocessing builder instance
        '''
        auth_operations = set(self.authorized_preprocessing_operations)
        for op in operations:
            auth_operations.add(models.PreprocessingOperationType(op.to_preproc_operation_type()))
        self.authorized_preprocessing_operations = list(auth_operations)


    def add_authorized_query(self,query:str):
        '''
        add_authorized_query adds the datasource query to the set of authorized queries

        Args:
            query (str): the data source query string
        '''
        queries = set(self.authorized_data_source_queries)
        queries.add(query)
        self.authorized_data_source_queries = list(queries)

    @staticmethod
    def __new_threshold(relative:bool=False,fixed_value:int=10,relative_factor:float=0.2) -> models.Threshold:
        if relative:
            threshold_type = models.ThresholdType.RELATIVE
        else:
            threshold_type = models.ThresholdType.FIXED
        return models.Threshold(fixed_value=fixed_value,relative_factor=relative_factor,type=threshold_type)


    def set_max_columns(self,relative:bool=False,fixed_value:int=5,relative_factor:float=0.2):
        '''
        set_max_columns Sets the maximum number of columns that can be input to the computation

        Args:
            relative (bool, optional): whether or not the maximum value is relative to the dataset size. Defaults to False.
            fixed_value (int, optional): absolute maximum value when not relative. Defaults to 5.
            relative_factor (float, optional): factor of the dataset size when relative. Defaults to 0.2.
        '''
        self.dp_policy.max_column_count = self.__new_threshold(relative,fixed_value,relative_factor)


    def set_min_frequencies(self,relative:bool=False,fixed_value:int=10,relative_factor:float=0.2):
        '''
        set_min_frequencies Sets the minimum number of frequencies required when the input dataset is used for counting
        The backend computation will verify that, for each numerical column, the sum of values is

        Args:
            relative (bool, optional): whether the threshold is relative or not. Defaults to False.
            fixed_value (int, optional): fixed value for the threshold. Defaults to 10.
            relative_factor (float, optional): the factor of the dataset size when the threshold is relative. Defaults to 0.2.
        '''
        self.dp_policy.min_frequencies = self.__new_threshold(relative,fixed_value,relative_factor)

    def set_max_factor(self,relative:bool=False,fixed_value:int=10,relative_factor:float=0.2):
        '''
        set_max_factor Sets the maximum number of factors any column can take as input
        Args:
            relative (bool, optional): whether the threshold is relative or not. Defaults to False.
            fixed_value (int, optional): fixed value for the threshold. Defaults to 10.
            relative_factor (float, optional): the factor of the dataset size when the threshold is relative. Defaults to 0.1.
        '''
        self.dp_policy.max_factors = self.__new_threshold(relative,fixed_value,relative_factor)


    def set_output_noise(self,eps: float=1,sensitivity:float=1,discrete:bool = False,delta: float=0.0001):
        '''
        set_output_noise sets the noise parameters. when set, every computation output gets encrypted noise added to it.
        If the noise is non discrete, then the laplacian mechanism is used, otherwise the gaussian mechanism is used

        Args:
            eps (float, optional): the value for the epsilon (privacy budget parameter). Defaults to 1.
            sensitivity (float, optional): the sensitivity parameter should be equal to the maximum difference expected between two neighboring datasets. Defaults to 1.
            discrete (bool, optional): whether or not the noise should be discretized
            delta (float,optional): the delta value when the noise is discrete
        '''
        self.dp_policy.noise_parameters = models.NoiseParameters(epsilon=eps,sensitivity=sensitivity,discrete=discrete,delta=delta)



displayed_labels = {
    'validateParameters': 'template validation',
    'fixedParameters': 'fixed',
    'flexibleParameters': 'flexible',
    'restrictDataSourceQueries': 'validate queries',
    'authorizedDataSourceQueries': 'authorized queries',
    'restrictPreprocessingOperations': 'validate operations',
    'authorizedPreprocessingOperations': 'authorized operations',
    'consideredVariables': 'authorized variables',
    'minDatasetSize': 'min rows',
    'minFrequencies': 'min frequencies',
    'maxColumnCount': 'max columns',
    'noiseParameters': 'noise',
}


def display_policy(p: models.ComputationPolicy,detailed: bool = False,show_queries: bool = False):
    display(Markdown('### Workflow Restrictions'))
    if not p.restrict_data_source_queries and not p.restrict_preprocessing_operations:
        display(Markdown("No workflow restrictions are set"))
    if p.restrict_preprocessing_operations:
        display(Markdown(f"Set of restricted preprocessing operations: `{[op.value for op in p.authorized_preprocessing_operations]}`"))
    if p.restrict_data_source_queries:
        display(Markdown("The policy only allows for limited queries on the data source"))
        if show_queries:
            display(Markdown('#### Authorized Queries'))
            for q in p.authorized_data_source_queries:
                display(Markdown(f'```sql\n{q}```\n'))
    if not isinstance(p.dp_policy,Unset):
        dp = p.dp_policy
        display_dp_policy(dp)
    if detailed:
        display(Markdown('### Detailed Policy (JSON)'))
        dict_values = p.to_dict()
        dict_values.pop('authorizedDataSourceQueries')
        json_formatted_str = json.dumps(dict_values, indent=2)
        display(Markdown("```\n" + json_formatted_str + "\n ```"))



def display_threshold(text:str,t: models.Threshold):
    if t.type == models.ThresholdType.FIXED:
        display(Markdown(f'{text}: ${t.fixed_value}$'))
    else:
        display(Markdown(f'{text}: ${t.relative_factor} N$ (where $N$ is the local dataset size) '))


def display_dp_policy(dp : models.DPPolicy):
    display(Markdown('### Disclosure Prevention Mechanisms'))
    params_set = False
    if isinstance(dp.authorized_variables,list) and len(dp.authorized_variables) > 0:
        params_set = True
        display(Markdown(f'Set of authorized variables: `{dp.authorized_variables}` _(any non-matching variable is automatically dropped)_'))
    if not isinstance(dp.min_dataset_size,Unset):
        params_set = True
        display(Markdown(f'minimum local dataset size: ${dp.min_dataset_size}$'))
    if not isinstance(dp.min_global_dataset_size,Unset):
        params_set = True
        display(Markdown(f'minimum global dataset size: ${dp.min_global_dataset_size}$'))
    if not isinstance(dp.min_frequencies,Unset):
        params_set = True
        display(Markdown('#### Minimum Frequencies'))
        display_threshold("Threshold",dp.min_frequencies)
        display(Markdown('This ensures that any Frequency $F$ is such that $F = 0$ or $F = N$ or $T <= F <= N - T$, where $N$ is the local dataset size and $T$ is the value of the threshold'))
    if not isinstance(dp.max_column_count,Unset):
        params_set = True
        display(Markdown('#### Maximum Number of Columns'))
        display_threshold("Threshold",dp.max_column_count)
        display(Markdown('this limits the number of columns which can be created during the preprocessing, avoiding that a subsequent aggregation leaks individual information.'))
    if not isinstance(dp.max_factors,Unset):
        params_set = True
        display(Markdown('#### Maximum Number of Factors'))
        display_threshold("Threshold",dp.max_factors)
        display(Markdown('Verifies for each categorical variable that the number of factors does not exceed the threshold'))
    if not isinstance(dp.noise_parameters,Unset):
        params_set = True
        np = dp.noise_parameters
        noise_type = "Laplacian Mechanism"
        if np.discrete:
            noise_type = "Discretized Gaussian Mechanism"
        display(Markdown(f'#### Output Noise ({noise_type})'))
        display(Markdown(f'epsilon: ${np.epsilon}$ (privacy budget, ideally should be set to values $< 1$ to ensure enough privacy)'))
        display(Markdown(f'sensitivity: ${np.sensitivity}$ (maximum difference of result when computing over two neighboring datasets)'))
        if np.discrete:
            display(Markdown(f'delta: ${np.delta}$ (secondary noise parameters should be set to ~ $1 / N$ where $N$ is an expected dataset size)'))
    if not params_set:
        display(Markdown("No disclosure prevention mechanism is set"))
