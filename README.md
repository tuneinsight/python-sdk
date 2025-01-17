# Tune Insight Python SDK

This is the official Python SDK for the Tune Insight API. It can be used to interface with a Tune Insight instance. The SDK enables programmatic use of Tune Insight from Jupyter notebooks and integration with other softwares, and gives access to advanced features such as custom preprocessing algorithms and machine learning pipelines.

## Documentation

The [official documentation](https://dev.tuneinsight.com/docs/Usage/python-sdk/) gives a detailed explanation on how to use the SDK. The recommended starting point to learn how to use the SDK is with the [Quickstart notebook](https://github.com/tuneinsight/python-sdk/tree/main/examples/Quickstart.ipynb).

## Installation

The SDK is available on `pip`:

```bash
pip install tuneinsight
```

If instructed by your administrator, you might need to install a specific version (e.g., `xx.y`):

```bash
pip install tuneinsight==xx.y
```

Note that versions `0.13.1` and older are not available on `pip`: [contact us](tech-support@tuneinsight.com) to get packages for these versions.

It is recommended to set up a custom environment for the SDK, e.g. using [`conda`](https://anaconda.org/anaconda/conda).

### Testing your implementation

After installing the package, run the following command in your terminal.

```bash
test-ti-install
```

If your installation succeeded, you should see the following message:

```
# Package is available          ✅
# Cryptolib is available        ✅
The Tune Insight SDK is correctly installed.
```

Refer to the [troubleshooting](#troubleshooting) section if you see any ❌.

### Connecting to a server

To further test your implementation, you can open a Python interpreter (e.g. a Jupyter notebook), and run the following commands, replacing `api_url` and `frontend_client_id` with the appropriate values. This will open a browser window asking you to log in to your Tune Insight account.

```python
from tuneinsight import Diapason

client = Diapason.from_config(
    api_url="<api_url>/api", # The url of the Tune Insight API to which the client will connect.
    oidc_client_id="<frontend_client_id>", # This is the front client id given by Tune Insight in the Portal.
)

client.login()

client.healthcheck(error=True)
```

If all goes well, this should complete in a few seconds (after you have entered your login details). You now have everything you need to start using the SDK! The recommended next step is to run the [Quickstart notebook](https://github.com/tuneinsight/python-sdk/tree/main/examples/Quickstart.ipynb) to learn more about existing features.

## Troubleshooting

#### command not found: test-ti-install

The installation of the package did not work, or a version before `0.14.0.1` was installed. To check the installed version, run the following line in the terminal:

```bash
pip freeze | grep tuneinsight
```

The result should look like this:

```
tuneinsight==0.14.0
```

If you see a line that looks like this,

```
tuneinsight @ file:///path/to/file/tuneinsight-0.13.1-py3-none-any.whl#sha256=...
```

the SDK was installed directly from a `.whl` file, suggesting you are using an older version. You might need to install a more recent version, using `pip`:

`pip install tuneinsight==0.14.0`

#### Error: Could not load the cryptolib: contact your administrator.

This means that the installation succeeded, but the `cryptolib` module of the SDK could not be installed on your system. You can still use your installation, but some features will not be available.

This issue should also trigger a warning to help identify the cause.

- `Could not find the cryptolib library. Your platform might not be supported.`: this means that the precompiled binary of the cryptolib is not available, most likely because it was not compiled for your operating system and architecture. The SDK is available for all common OSes and architectures, but we can compile for additional architectures if necessary.
- `cannot open shared object file: ...`: the precompiled binary was found, but it could not be loaded by your system. This issue could be caused by a number of issues, so we suggest [reaching out to us](contact@tuneinsight.com).

#### Client is not allowed to initiate OAuth 2.0 Device Authorization Grant.

This error (which occurs when running `client.login`) suggests that the client or instance is not properly configured. Usually, this is caused by one of the following:

- The `frontend_client_id` you entered is not correct.
- Your Python environment can't connect to the authentication provider (https://auth.tuneinsight.com)
- The authentication configuration does not allow the use of the SDK. Contact your administrator.
- Your instance uses a different authentication provider. You will need to change the `oidc_url` argument in `Diapason.from_config`. Ask your administrator for the url that you should use (don't forget the `/auth/` at the end of the URL).

#### `client.login` hangs for some time after entering credentials.

This means that the login was succesful, but the client is not able to connect to the Tune Insight instance. An error message will typically appear after a minute or so. If you get the following error, it might just be that the `api_url` you entered was not correct:

```
httpx.ConnectError: [Errno -3] Temporary failure in name resolution
```

For other errors, contact your administrator: this might suggest that the instance is down or otherwise unavailable, or that there was an issue with the configuration.

#### API version mismatch: the server and client use different versions of the API.

This warning will not occur during the test script, but commonly occurs when using the SDK (specifically, creating or connecting to a project). It means that the version you installed is not consistent with the version of the Tune Insight instance you are connecting to.
Depending on the versions, this might not be too big of an issue, but it is strongly recommended to install the same version.
Ask your administrator for the version installed on the Tune Insight instance, and install the corresponding SDK version with

```bash
pip install tuneinsight==0.xx.y
```

## License

Apache License 2.0
