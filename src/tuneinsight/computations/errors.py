from typing import Tuple,List
from tuneinsight.utils.errors import hidden_traceback_scope

class DisclosurePreventionError(Exception):
    '''
    DisclosurePreventionError Exception class for the disclosure prevention error
    '''

    def __init__(self, message: str):
        self.message = f'computation aborted: {message}'
        super().__init__(self.message)


class PreprocessingError(Exception):
    '''
    PreprocessingError is used to represent error that happen during preprocessing
    '''
    def __init__(self, message: str):
        self.message = f'error while preprocessing: {message}'
        super().__init__(self.message)


class ComputationError(Exception):
    '''
    ComputationError is used represent any error that can happen during a computation
    '''
    def __init__(self, message: str):
        self.message = f'{message}'
        super().__init__(self.message)





dpm_error_pattern = "disclosure prevention error:"
'''pattern used for detecting disclosure prevention errors'''
preproc_error_pattern = "preprocessing error:"
'''pattern used for detecting preprocessing errors'''


patterns = {
    dpm_error_pattern: DisclosurePreventionError,
    preproc_error_pattern: PreprocessingError,
}
'''mapping from patterns to their appropriate exception'''



def parse_errors(errors : List[str]) -> str:
    '''
    parse_errors joins the errors using end of line separators

    Args:
        errors (List[str]): the list of errors

    Returns:
        str: the flattened error string
    '''
    return '\n'.join(errors)


def find_error_pattern(error_msg:str,pattern: str) -> Tuple[bool,str]:
    '''
    find_error_pattern checks whether the pattern is present in the error message.

    Args:
        error_msg (str): the flattened computation error
        pattern (str): the pattern to find

    Returns:
        Tuple[bool,str]: whether or not the pattern was found, the error message following the pattern
    '''
    if pattern in error_msg:
        msg = error_msg[error_msg.find(pattern) + len(pattern):]
        msg = msg[:msg.find('\n')]
        return True,msg
    return False,""

def raise_computation_error(errors: List[str]):
    '''
    raise_computation_error raises the appropriate given the list of errors from the computation and suppresses any traceback

    Args:
        errors (List[str]): the list of errors returned with the computation

    Raises:
        exc: the appropriate computation error when a common pattern is detected
        ComputationError: the default computation error when no common pattern is detected
    '''
    with hidden_traceback_scope():
        flat_error = parse_errors(errors)
        for pattern,exc in patterns.items():
            ok,msg = find_error_pattern(flat_error,pattern)
            if ok:
                raise exc(message=msg)
        raise ComputationError(message=flat_error)
