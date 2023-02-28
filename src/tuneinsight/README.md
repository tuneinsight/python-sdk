# Tune Insight Python SDK

Diapason is the Tune Insight Python SDK

## Getting Started

### Installing

```bash
pip install tuneinsight-0.1.1.tar.gz
```

## Usage

To use the SDK you must be able to connect to a *Tune Insight* Agent.


### Creating a client to the agents

To create a new client to one of the running agents, simply run:
```python
from tuneinsight.client.diapason import Diapason
client = Diapason.from_config_path('conf.yml')
```

## Documentation
The complete documentation for Diapason is available [here](https://docs.tuneinsight.com/docs/python-sdk).


## License
Apache License 2.0