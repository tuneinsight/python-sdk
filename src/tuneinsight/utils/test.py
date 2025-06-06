"""Utilities to test the installation of the SDK."""

from tuneinsight import Diapason
from tuneinsight.cryptolib import cryptolib


def _test_basic():
    """Checks that this works."""


def _test_cryptolib():
    """Checks that the cryptolib is supported on this platform."""
    cryptoparams_b64 = cryptolib.test_polynomial_evaluation_hefloat_params()
    crypto_id = cryptolib.new_hefloat_operator_from_b64_hefloat_parameters(
        cryptoparams_b64.decode("utf-8")
    )
    cryptolib.key_generation(crypto_id)


def _test_version():
    """Checks that the version is compatible with the latest install. Currently not enabled."""
    client = Diapason.from_config("https://stage-a-node-0.tuneinsight.net/", "cli")
    client.check_api_compatibility(hard=True)


def _test_jupyter():
    """Checks that Jupyter is installed (full install)."""
    import jupyter  # pylint: disable=import-error,unused-import,import-outside-toplevel


_INSTALL_TESTS = [
    (_test_basic, "Package is available  "),
    (_test_cryptolib, "Cryptolib is available"),
    # (_test_version, "Latest version installed"),
]

_OPTIONAL_TESTS = [
    (
        _test_jupyter,
        "Jupyter is available",
        "Jupyter is not installed, use `pip install tuneinsight[full]` to install it if needed.",
    )
]


def _run(f, description, failure_message=""):
    print(f"# {description}\t", end="")
    try:
        f()
    except Exception as err:  # pylint: disable=broad-exception-caught
        print("❌")
        if failure_message:
            print(f"\t{failure_message}")
        else:
            print("\tError:", str(err))
        return False
    print("✅")
    return True


def test_install():
    """Runs simple tests to check that the installation is correct."""
    all_success = True
    for f, description in _INSTALL_TESTS:
        all_success = _run(f, description) and all_success
    if all_success:
        print("The Tune Insight SDK is correctly installed.")
    else:
        print(
            "Your installation is not correct, see https://github.com/tuneinsight/python-sdk for troubleshooting help."
        )
    print("\nChecking optional packages:")
    for f, description, failure_message in _OPTIONAL_TESTS:
        _run(f, description, failure_message)
