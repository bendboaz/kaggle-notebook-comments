from abc import ABC, abstractmethod

from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator, ClassifierMixin


class BaseNotebooksModel(ABC, BaseEstimator, ClassifierMixin):
    def __init__(self):
        super(BaseNotebooksModel, self).__init__()

    @abstractmethod
    def fit(self, X: ArrayLike, y: ArrayLike):
        pass

    @abstractmethod
    def predict(self, X: ArrayLike) -> ArrayLike:
        pass
