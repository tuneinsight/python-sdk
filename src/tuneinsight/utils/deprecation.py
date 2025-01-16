"""Internal utilities to handle deprecation messages nicely."""

import warnings

DEPRECATION_VERSION = "0.15.0"
MESSAGE = "⚠️ {} is deprecated and will be removed in the next major version (v{})."
RECOMMENDATION = " 👉 Use {} instead."
BREAKING = " 🚫 A breaking change was introduced: please update your code now."


def warn(
    old_function, recommended_function=None, breaking=False, version=DEPRECATION_VERSION
):
    """Warns the user that the code they are using is deprecated and give a recommendation."""
    message = MESSAGE.format(old_function, version)
    if recommended_function is not None:
        message += RECOMMENDATION.format(recommended_function)
    if breaking:
        message += BREAKING
    warnings.warn(message)
