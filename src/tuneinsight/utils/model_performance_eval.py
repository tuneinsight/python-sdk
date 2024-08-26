"""
Utilities to measure the performances of a machine learning model.

The metrics defined in this module all take two arguments: y_true (the
true label) and y_pred (the predicted label), two arrays or array-like
of the same shape. They function similarly to their implementation in
sklearn.metrics, but without the dependency on scikit-learn.

"""

from typing import List
import numpy as np


def _check_arrays(y_true: List[float], y_pred: List[float]):
    """
    Check that inputs can be cast to np.arrays of the same size.

    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    assert (
        y_true.shape == y_pred.shape
    ), f"Input arrays have mismatching dimensions ({y_true.shape} >< {y_pred.shape})."
    return y_true, y_pred


def mse(y_true: List[float], y_pred: List[float]) -> float:
    """Computes the mean square error (same as sklearn.metrics.mse)."""
    y_true, y_pred = _check_arrays(y_true, y_pred)
    return np.square(y_true - y_pred).mean()


def rmse(y_true: List[float], y_pred: List[float]) -> float:
    """Computes the root mean square error (same as sklearn.metrics.rmse)."""
    return np.sqrt(mse(y_true, y_pred))


def r2_score(y_true: List[float], y_pred: List[float]) -> float:
    """Computes the R2 score  (same as sklearn.metrics.mse)."""
    y_true, y_pred = _check_arrays(y_true, y_pred)

    ss_t = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_r = np.sum((y_true - y_pred) ** 2)

    return 1 - (ss_r / ss_t)


def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Applies the sigmoid activation on an array.

    Args:
        z (np.ndarray): the numpy representation of z

    Returns:
        np.ndarray: the transformed array
    """
    return 1 / (1 + np.exp(-z))


def regression_prediction(
    weights: np.ndarray,
    bias: np.ndarray,
    inputs: np.ndarray,
    activation: callable = None,
) -> np.ndarray:
    """
    Computes the regression prediction given the weights, bias and input datasets.

    An additional optional activation function can be provided to be applied after
    the linear transformation.

    Args:
        weights (np.ndarray): the model weights/coefficients
        bias (np.ndarray): the model bias
        inputs (np.ndarray): the input dataset
        activation (callable, optional): the optional activation function. Defaults to None.

    Returns:
        np.ndarray: the numpy array of predicted values
    """
    z = np.dot(weights.T, inputs.T) + bias
    if activation is not None:
        return activation(z)
    return z


def accuracy(y_true: np.ndarray, y_scores_pred: np.ndarray, threshold=0.5):
    """
    Computes the accuracy of a binary prediction.

    Args:
        y_true: the truth array, an array of {0, 1}.
        y_scores_pred: the *scores* predicted by a classifier, typically in [0, 1].
        threshold: the threshold for the scores (scores above it are considered a prediction of 1).
    """
    y_true = y_true.astype(float) >= threshold
    y_pred = y_scores_pred >= threshold
    return np.mean(y_true == y_pred)
