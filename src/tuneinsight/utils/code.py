"""Utilities to read and package Python code to be sent."""

import inspect
import textwrap


def get_code(function):
    """Returns the cleaned code for a Python function.

    The cleaning involves (1) dedenting the code so that the `def` statement is not
    indented, and (2) removing all decorators.

    """
    # Fetch and dedent the code of the custom function.
    function_code = textwrap.dedent(inspect.getsource(function))
    # inspect.getsource also fetches decorators around the function. We remove these, as (1) this can cause issues, since
    # the decorator code is not sent, (2) we have custom decorators implemented in remotedf.
    lines = function_code.split("\n")
    cutoff = 0
    for i, line in enumerate(lines):
        if line.startswith("def "):
            cutoff = i
            break
        # Ensure we are not cutting any non-decorator code.
        assert line.startswith("@"), "Non-decorator line before function declaration"
    return "\n".join(lines[cutoff:])
