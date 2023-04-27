from typing import List
import math
import numpy as np

def mse(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return np.square(np.subtract(y_true,y_pred)).mean()

def rmse(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return math.sqrt(mse(y_true,y_pred))

def r2_score(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    if len(y_pred) != len(y_true):
        raise Exception("Input sizes should be equal")
    size = len(y_pred)

    ss_t = 0
    ss_r = 0

    mean_y = np.mean(y_true)

    for i in range(size):
        ss_t += (y_true[i] - mean_y) ** 2
        ss_r += (y_true[i] - y_pred[i]) ** 2

    r2 = 1 - (ss_r/ss_t)
    return r2
