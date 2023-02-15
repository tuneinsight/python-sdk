# Tune Insight Python SDK

Diapason is the Tune Insight Python SDK

## Getting Started

### Installing

```bash
pip install tuneinsight-0.1.0.tar.gz
```

## Usage

To use the SDK you must be able to connect to a *Tune Insight* Agent.


### Creating a client to the agents

To create a new client to one of the running agents, simply run:
```python
from tuneinsight.client.diapason import Diapason
client = Diapason.from_config_path('conf.yml')
```

### Features
#### Computations
#### Preprocessing
Preprocessing operations should be defined in relation to a computation. The preprocessing when the computation is ran.
For example:
```
aggregation = project.new_enc_aggregation()
aggregation.preprocessing.one_hot_encoding(target_column='gender', prefix='', specified_types=['Male', 'Female'])
```

Preprocessing operations can be applied to all nodes or specific nodes if the data format is different across nodes. This requires using the `nodes` argument, as follows:
```
aggregation.preprocessing.one_hot_encoding(target_column='gender', prefix='', specified_types=['Male', 'Female'], nodes=['Organization_A'])
aggregation.preprocessing.one_hot_encoding(target_column='genre', prefix='', specified_types=['Male', 'Female'], nodes=['Organization_B'])
aggregation.preprocessing.one_hot_encoding(target_column='genero', prefix='', specified_types=['Male', 'Female'], nodes=['Organization_C'])
```

##### Select
Select specified columns from data.
```
select(columns, create_if_missing, dummy_value, nodes)
```
* `columns` : list of column names to be selected (`List[str]`)
* `create_if_missing` : whether to create the columns if they do not exist, default = False (`bool`)
* `dummy_value` : what to fill the created columns with, default = "" (`str`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### One Hot Encoding
Encodes a target column into one hot encoding and extends the table with these columns
```
one_hot_encoding(target_column, prefix, specified_types, nodes)
```
* `target_column` : name of column to convert to one-hot-encoding (`str`)
* `prefix` : prefix string to prepend to one-hot column names (`str`)
* `specified_types` : specified types to one-hot encode, if specified, then possible missing columns will be added (`List[str]`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Filter
Filters rows from the data under a given condition
```
filter(target_column, comparator, value, numerical, nodes)
```
* `target_column` : name of column to filter on (`str`)
* `comparator` : type of comparison (`ComparisonType` enum)

	* equal
	* nEqual
	* greater
	* greaterEq
	* less
	* lessEq
	* in

* `value` : value with which to compare (`str`)
* `numerical` : whether the comparison is on numerical values, default = False (`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Counts
Concatenates a new column containing 1 for each row in order to count the number of rows
```
counts(output_column_name, nodes)
```
* `output_column_name` : name of the column to store the counts. If not specified, the name 'count' will be used. (`str`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Transpose
Transpose index and columns
```
transpose(copy, nodes)
```
* `copy` : Whether to copy the data after transposing. default False (`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Set Index
Set the DataFrame index using existing columns.
```
set_index(cols, drop, append, nodes)
```
* `columns` : list of column names to set as index (`List[str]`)
* `drop` : Delete columns to be used as the new index. default True (`bool`)
* `append` : Whether to append columns to existing index. default False (`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Reset Index
Reset the index, or a level of it.
```
reset_index(level, drop, nodes)
```
* `level` : list of column names to remove from index (`List[str]`)
* `drop` : Do not try to insert index into dataframe columns. This resets the index to the default integer index. default False (`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Rename
Alter axes labels.
```
rename(mapper, axis, copy, errors, nodes)
```
* `mapper` : Dict of transformations to apply to that axis’ values. (`dict`)
* `axis` : Axis to target with `mapper`. Should be the axis name (‘index’, ‘columns’). The default is ‘index’. (`RenameAxis`)
* `copy` : Also copy underlying data. default True (`bool`)
* `errors` : If True raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If False existing keys will be renamed and extra keys will be ignored.(`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### As Type
Cast column types
```
astype(type_map, copy, errors, nodes)
```
* `mapper` : Dict which maps column names to dtypes. (`dict`)
* `copy` : Return a copy. default True (`bool`)
* `errors` : If True raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If False existing keys will be renamed and extra keys will be ignored.(`bool`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

##### Extract Dict Field
Extract field value from dict-like columns
```
extract(field, columns, names, nodes)
```
* `field` : dict field to extract (`str`)
* `columns` : list of column names from which to extract field (`List[str]`)
* `names`: names of resulting columns, if None, no new columns are created (`List[str]`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)

For example given:
 | id | dict_col |
 | -- | -- |
 | 0 | { 'foo' : 3, 'bar' : 0.56} |
 | 1 | { 'foo' : 8, 'bar' : 0.22} |
 | 2 | { 'foo' : 5, 'bar' : 0.13} |

`extract(field='foo', columns=['dict_col'])` yields:
 | id | dict_col |
 | -- | -- |
 | 0 | 3 |
 | 1 | 8 |
 | 2 | 5 |

##### Apply RegEx
Apply a RegEx mapping to columns
```
apply_regex(regex, columns, regex_type, names, nodes)
```
* `regex` : regular expression to apply (`str`)
* `columns` : list of column names from which to extract field (`List[str]`)
* `regex_type` : defines what we want to retrieve from the regex (`ApplyRegExType`)
	* `ApplyRegExType.MATCH` : return the first match
	* `ApplyRegExType.FINDALL`: return list of matching values
	* `ApplyRegExType.POSITION`: return position of first match
* `names`: names of resulting columns, if None, no new columns are created (`List[str]`)
* `nodes` : which nodes to apply the preprocessing operation to, if `None` it will apply to all (`List[str]`)


## License
Apache License 2.0