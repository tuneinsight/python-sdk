## How to implement new computations

New computations should be made available to users by creating dedicated classes inheriting from `tuneinsight.computations.base.Computation`. There are two main scenarios:

1. either your computation is defined by a single API model;
2. or it is not (e.g., one of two models is used depending on some parameters).

The former (and simpler) case can be implemented by extending the `ModelBasedComputation` class, whereas the latter will have to extend the lower-level `Computation` class. We will first focus on how to do the former, and touch on the latter later.

Your new class, inheriting from `ModelBasedComputation`, must essentially define two parts:

1. the parameters that need to be set for your computation;
2. additional pre-/post-processing operations specific to your computation.

### Computation parameters

Computation parameters are ideally set through the constructor (even though `ModelBasedComputation` provides `__setattr__` to modify the model directly). The constructor should also set the `model` and `type` of the computation so that these are not exposed to the user.

For instance, let's assume we have a `ShiftedSum` operation which adds together the values of a selected variable `variable`, then optionally adds a value `shift` to the result. The class created for it would look like this (in, say, `tuneinsight/computations/shiftedsum.py`):

```python
class ShiftedSum(ModelBasedComputation):
    def __init__(self, project, variable, shift=UNSET, **kwargs):
        super().__init__(
            project,
            model_class=models.ShiftedSum,
            type=models.ComputationType.SHIFTEDSUM,
            variable=variable,
            shift=shift,
            **kwargs
        )
```

Passing `kwargs` is not necessary, but is a good idea to enable users to impose custom settings if they want.

In some cases, API models require some parameters to take values of specific API classes that are not very user-friendly. In this case, you should allow users to provide user-friendly inputs, then pre-process those inputs by instantiating the API classes from the user inputs. A natural place to do this is either in user input methods that set these values (e.g., `set_complex_input()`), in the constructor, or as a last resort in the `._get_model` method (that is called before any use of the model, and by default just returns `self.model`).

Also, if your class implements differential privacy, don't forget to include `dp_epsilon: float = None` as an argument! This parameter is part of all computation definitions, but is the only one that users are expected to change.

**Note** -- the `super().__init__` call PATCHes the project with the new computation definition. Hence, it should be done _after_ setting internal variables of the `Computation` object (preferably at the end of the constructor).

### Pre-/post-processing

Users interact with computations mostly by calling `.run`. By default, this interface is relatively low-level, returning a list of data objects (potentially still encrypted). To make this interface friendlier, implement the `._process_results` method (that is called by `Computation.run`). For instance, for shifted sum (where the answer is a scalar):

```python
class ShiftedSum(Computation):
    # ...

    def _process_results(self, results: List[_Content]) -> float:
        return results[0].get_float_matrix()[0]
```

The input of this function is a list (typically of length 1) of objects inheriting from `dataobject._Content` (which provides methods to convert to common data types such as dataframe and float matrix). Specifically, these will most of the time be instances of `dataobject.Result`, but could also be `dataobject.DataObject` (for legacy reasons).

You may also override `_pre_run_check` (which is called at the beginning of `.run`) to check that the configuration is acceptable for a run. This allows you to display user-friendly failure messages (or implement failsafe default values). This can also be a place to change specific settings prior to a run (such as the timeout, for long computations).

For more complex operations, it can make sense to override the `.run` method directly. Note that `Computation.run(shifted_sum)` will always work (and use the default `run` interface), so it is not necessary to "keep" a low-level interface on a high-level object. Just override `.run` to have a user-friendly interface, and instruct users to use `Computation.run` if they really need to re-use the same interface as other computations.

### Enable computation fetching

The `Project` class has a `get_computation` method that retrieves the API model for the computation currently set on the project and returns a `tuneinsight.Computation` object. In order to enable this with your new computation, you should first add it in `computations/types.py` in three places: the `Type` enum, the `displayed_types` dictionary mapping to a human-readable name, and the `type_to_class` dictionary mapping the type to your new class. Then, you must implement a `from_model` class that instantiates your new class based on an API model. This method doesn't need to do anything fancy: it should just set internal variables of the class to be consistent with the model, so that it is consistent with the computation in the backend. The easiest way to do this is through the constructor of your class (`__init__`), passing the values in the model as input parameters.

### Additional tools

Your new `Computation` class is also a great place to put all the code related to the analysis of the results, such as plots. If the results output by your class are particularly complicated, it can make sense to implement a specific results class (`ShiftedSumResults` -- the name can be wordy as it will never be instantiated by users) that has methods for plotting etc. While you are free to do what you want here, it is recommended to extend the `tuneinsight.computations.base.ComputationResult` abstract class in order to have a unified interface across computations. See the `computations/stats.py` module for an example.

### Documentation

Please remember to include docstrings describing what the computation does (at the class level), what its inputs are (including parameters, in docstrings for the constructor `__init__`), and what its outputs are (in docstrings for `.run`). These will serve as documentation :) (literally, these are rendered in the online documentation for users).

### Inheriting from `Computation` directly

Under the hood, `Computation` is an abstract class that defines many common operations over computations, and has an abstract method `._get_model()` that returns an API model for this computation (except for high-level parameters like preprocessing, which are defined by `Computation` itself). `ModelBasedComputation` extends `Computation` and implements the `._get_model` method by returning `self.model` (one specific model, of a class specified in the constructor). This makes it easy to configure the computation by modifying the model directly, but assumes that the computation can be described by one and only one model. In some cases, it can make sense to allow the model to be created dynamically whenever `._get_model` is called, e.g., if multiple model classes could be appropriate.

To create a class inheriting from `Computation`, you must:

1. Implement `._get_model` appropriately. This method cannot take arguments, and its output cannot be modified before the model is used. Hence, you must provide all additional configuration to the Computation object beforehand (typically, in the constructor of your new class).
2. Implement additional post-processing (`._process_results`) etc. as above.
3. Document very clearly to the user what you did: your class has a different interface from others in the SDK, so its usage should be clearly documented.
