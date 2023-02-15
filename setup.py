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
 'tuneinsight.api.sdk.api.api_project',
 'tuneinsight.api.sdk.api.api_protocols',
 'tuneinsight.api.sdk.api.api_query',
 'tuneinsight.api.sdk.api.api_sessions',
 'tuneinsight.api.sdk.api.health',
 'tuneinsight.api.sdk.api.metrics',
 'tuneinsight.api.sdk.models',
 'tuneinsight.client',
 'tuneinsight.computations',
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
    'version': '0.1.0',
    'description': 'Diapason is the official Python SDK for the Tune Insight Agent API',
    'long_description': '# Tune Insight Python SDK\n\nDiapason is the Tune Insight Python SDK\n\n## Getting Started\n\n### Installing\n\n```bash\npip install tuneinsight-0.1.0.tar.gz\n```\n\n## Usage\n\nTo use the SDK you must be able to connect to a *Tune Insight* Agent.\n\n\n### Creating a client to the agents\n\nTo create a new client to one of the running agents, simply run:\n```python\nfrom tuneinsight.client.diapason import Diapason\nclient = Diapason.from_config_path(\'conf.yml\')\n```\n\n### Features\n#### Computations\n#### Preprocessing\nPreprocessing operations should be defined in relation to a computation. The preprocessing when the computation is ran.\nFor example:\n```\naggregation = project.new_enc_aggregation()\naggregation.preprocessing.one_hot_encoding(target_column=\'gender\', prefix=\'\', specified_types=[\'Male\', \'Female\'])\n```\n\nPreprocessing operations can be applied to all nodes or specific nodes if the data format is different across nodes. This requires using the `nodes` argument, as follows:\n```\naggregation.preprocessing.one_hot_encoding(target_column=\'gender\', prefix=\'\', specified_types=[\'Male\', \'Female\'], nodes=[\'Organization_A\'])\naggregation.preprocessing.one_hot_encoding(target_column=\'genre\', prefix=\'\', specified_types=[\'Male\', \'Female\'], nodes=[\'Organization_B\'])\naggregation.preprocessing.one_hot_encoding(target_column=\'genero\', prefix=\'\', specified_types=[\'Male\', \'Female\'], nodes=[\'Organization_C\'])\n```\n\n##### Select\nSelect specified columns from data.\n```\nselect(columns, create_if_missing, dummy_value, nodes)\n```\n* `columns` : list of column names to be selected (`List[str]`)\n* `create_if_missing` : whether to create the columns if they do not exist, default = False (`bool`)\n* `dummy_value` : what to fill the created columns with, default = "" (`str`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### One Hot Encoding\nEncodes a target column into one hot encoding and extends the table with these columns\n```\none_hot_encoding(target_column, prefix, specified_types, nodes)\n```\n* `target_column` : name of column to convert to one-hot-encoding (`str`)\n* `prefix` : prefix string to prepend to one-hot column names (`str`)\n* `specified_types` : specified types to one-hot encode, if specified, then possible missing columns will be added (`List[str]`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Filter\nFilters rows from the data under a given condition\n```\nfilter(target_column, comparator, value, numerical, nodes)\n```\n* `target_column` : name of column to filter on (`str`)\n* `comparator` : type of comparison (`ComparisonType` enum)\n\n\t* equal\n\t* nEqual\n\t* greater\n\t* greaterEq\n\t* less\n\t* lessEq\n\t* in\n\n* `value` : value with which to compare (`str`)\n* `numerical` : whether the comparison is on numerical values, default = False (`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Counts\nConcatenates a new column containing 1 for each row in order to count the number of rows\n```\ncounts(output_column_name, nodes)\n```\n* `output_column_name` : name of the column to store the counts. If not specified, the name \'count\' will be used. (`str`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Transpose\nTranspose index and columns\n```\ntranspose(copy, nodes)\n```\n* `copy` : Whether to copy the data after transposing. default False (`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Set Index\nSet the DataFrame index using existing columns.\n```\nset_index(cols, drop, append, nodes)\n```\n* `columns` : list of column names to set as index (`List[str]`)\n* `drop` : Delete columns to be used as the new index. default True (`bool`)\n* `append` : Whether to append columns to existing index. default False (`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Reset Index\nReset the index, or a level of it.\n```\nreset_index(level, drop, nodes)\n```\n* `level` : list of column names to remove from index (`List[str]`)\n* `drop` : Do not try to insert index into dataframe columns. This resets the index to the default integer index. default False (`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Rename\nAlter axes labels.\n```\nrename(mapper, axis, copy, errors, nodes)\n```\n* `mapper` : Dict of transformations to apply to that axis’ values. (`dict`)\n* `axis` : Axis to target with `mapper`. Should be the axis name (‘index’, ‘columns’). The default is ‘index’. (`RenameAxis`)\n* `copy` : Also copy underlying data. default True (`bool`)\n* `errors` : If True raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If False existing keys will be renamed and extra keys will be ignored.(`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### As Type\nCast column types\n```\nastype(type_map, copy, errors, nodes)\n```\n* `mapper` : Dict which maps column names to dtypes. (`dict`)\n* `copy` : Return a copy. default True (`bool`)\n* `errors` : If True raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If False existing keys will be renamed and extra keys will be ignored.(`bool`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n##### Extract Dict Field\nExtract field value from dict-like columns\n```\nextract(field, columns, names, nodes)\n```\n* `field` : dict field to extract (`str`)\n* `columns` : list of column names from which to extract field (`List[str]`)\n* `names`: names of resulting columns, if None, no new columns are created (`List[str]`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\nFor example given:\n | id | dict_col |\n | -- | -- |\n | 0 | { \'foo\' : 3, \'bar\' : 0.56} |\n | 1 | { \'foo\' : 8, \'bar\' : 0.22} |\n | 2 | { \'foo\' : 5, \'bar\' : 0.13} |\n\n`extract(field=\'foo\', columns=[\'dict_col\'])` yields:\n | id | dict_col |\n | -- | -- |\n | 0 | 3 |\n | 1 | 8 |\n | 2 | 5 |\n\n##### Apply RegEx\nApply a RegEx mapping to columns\n```\napply_regex(regex, columns, regex_type, names, nodes)\n```\n* `regex` : regular expression to apply (`str`)\n* `columns` : list of column names from which to extract field (`List[str]`)\n* `regex_type` : defines what we want to retrieve from the regex (`ApplyRegExType`)\n\t* `ApplyRegExType.MATCH` : return the first match\n\t* `ApplyRegExType.FINDALL`: return list of matching values\n\t* `ApplyRegExType.POSITION`: return position of first match\n* `names`: names of resulting columns, if None, no new columns are created (`List[str]`)\n* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)\n\n\n## License\nApache License 2.0',
    'author': 'Tune Insight SA',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
