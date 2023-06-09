# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tuneinsight',
 'tuneinsight.api',
 'tuneinsight.api.sdk',
 'tuneinsight.api.sdk.api',
 'tuneinsight.api.sdk.api.api_admin',
 'tuneinsight.api.sdk.api.api_computations',
 'tuneinsight.api.sdk.api.api_dataobject',
 'tuneinsight.api.sdk.api.api_datasource',
 'tuneinsight.api.sdk.api.api_log',
 'tuneinsight.api.sdk.api.api_ml',
 'tuneinsight.api.sdk.api.api_network',
 'tuneinsight.api.sdk.api.api_private_search',
 'tuneinsight.api.sdk.api.api_project',
 'tuneinsight.api.sdk.api.api_protocols',
 'tuneinsight.api.sdk.api.api_query',
 'tuneinsight.api.sdk.api.api_sessions',
 'tuneinsight.api.sdk.api.health',
 'tuneinsight.api.sdk.api.metrics',
 'tuneinsight.api.sdk.models',
 'tuneinsight.client',
 'tuneinsight.computations',
 'tuneinsight.cryptolib',
 'tuneinsight.utils']

package_data = \
{'': ['*'], 'tuneinsight.utils': ['graphical/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'attrs>=21.3.0',
 'docker>=6.0.1,<7.0.0',
 'httpx>=0.15.4,<0.24.0',
 'matplotlib>=3.6.0,<4.0.0',
 'notebook>=6.4.11,<7.0.0',
 'pandas>=1.4.2,<2.0.0',
 'pylint>=2.15.2,<3.0.0',
 'python-dateutil>=2.8.0,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'python-keycloak>=0.27.0,<0.28.0',
 'pyvcf3>=1.0.3,<2.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'seaborn>=0.12.1,<0.13.0',
 'wheel>=0.37.1,<0.38.0']

setup_kwargs = {
    'name': 'tuneinsight',
    'version': '0.4.0',
    'description': 'Diapason is the official Python SDK for the Tune Insight Agent API',
    'long_description': "# Tune Insight Python SDK\n\nDiapason is the Tune Insight Python SDK\n\n## Getting Started\n\n### Installing\n\n```bash\npip install tuneinsight-0.4.0.tar.gz\n```\n\n## Usage\n\nTo use the SDK you must be able to connect to a *Tune Insight* Agent.\n\n\n### Creating a client to the agents\n\nTo create a new client to one of the running agents, simply run:\n```python\nfrom tuneinsight.client.diapason import Diapason\nclient = Diapason.from_config_path('conf.yml')\n```\n\n## Documentation\nThe complete documentation for Diapason is available [here](https://docs.tuneinsight.com/docs/python-sdk).\n\n\n## License\nApache License 2.0",
    'author': 'Tune Insight SA',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
