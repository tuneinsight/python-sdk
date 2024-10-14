"""
# Interacting with a Tune Insight instance

The `client` module offers high-level classes to interact with the various
elements of a Tune Insight instance. 

## Connecting to a Tune Insight instance

The [`Diapason`](https://dev.tuneinsight.com/docs/Usage/python-sdk/reference_docs/client/diapason/#diapason)
class is the client used to connect to a Tune Insight instance. The code used
to initialize a client and connect to the instance is typically:

```python
from tuneinsight import Diapason

client = Diapason.from_config(
    api_url="<api_url>/api", # The url of the Tune Insight API.
    oidc_client_id="<frontend_client_id>", # Frontend client id given by Tune Insight in the Portal.
)

client.login()  # This will open a browser window asking you to log in.
```

Consult [the documentation](https://dev.tuneinsight.com/docs/Usage/python-sdk/client-configuration/)
for more details, connection options, and troubleshooting.

## Project management

Collaborations in Tune Insight instances occur through projects. Projects bring together the
various parts of a collaboration: defining computations, linking data to computations, and enforcing
privacy policies. In the SDK, projects can be interacted with through the `client.Project` class.

[The documentation](https://dev.tuneinsight.com/docs/Usage/python-sdk/projects/) details how to create,
setup, and manage a project.

## Data management

Data in Tune Insight instances is stored with two different abstractions:

- Datasources (`client.datasource`) represent data to be used for computations. Datasources can be of
    different types (e.g., API, database). The data containted in a datasource is only loaded when a
    computation starts.
- Dataobjects (`client.dataobject`) represent values stored on the instance, typically as the result
    of a computation. These can be downloaded and read from the SDK client.

_Note_: most operations do not involve _any_ data transfer from the Tune Insight instance to the SDK client.
Private data remains securely stored on the instance.

The documentation on datasource management is available [here](https://dev.tuneinsight.com/docs/Usage/python-sdk/data-management/).

"""

# This module imports a subset of the classes defined by tuneinsight.client.*
# submodules, focusing on those intended to be used for high-level interaction
# with the instance.

from .dataobject import DataObject, Result
from .datasource import DataSource
from .diapason import Diapason
from .project import Project
from .session import PIRSession
