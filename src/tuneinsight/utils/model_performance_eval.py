from typing import List
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt


def accuracy(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return metrics.accuracy_score(y_true, y_pred, normalize=True)

def recall(y_true: List[float]=None, y_pred: List[float]=None, average: str="macro") -> float:
    return metrics.recall_score(y_true, y_pred, average=average)

# F1 = 2 * (precision * recall) / (precision + recall)
def f1_score(y_true: List[float]=None, y_pred: List[float]=None, average: str="macro") -> float:
    return metrics.f1_score(y_true, y_pred, average=average)

def r2_score(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return metrics.r2_score(y_true, y_pred)

def mse(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return metrics.mean_squared_error(y_true, y_pred)

def rmse(y_true: List[float]=None, y_pred: List[float]=None) -> float:
    return metrics.mean_squared_error(y_true, y_pred, squared=False)

def confusion_matrix(y_true: List[float]=None, y_pred: List[float]=None):
    cm = metrics.confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(9,9))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    all_sample_title = 'Confusion matrix'
    plt.title(all_sample_title, size = 15)
    plt.show()
