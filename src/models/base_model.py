from abc import ABC, abstractmethod
from typing import List

from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator, ClassifierMixin

from src.types.notebook import Notebook


class BaseNotebooksModel(ABC, BaseEstimator, ClassifierMixin):
    def __init__(self):
        super(BaseNotebooksModel, self).__init__()

    @abstractmethod
    def fit(self, X: List[Notebook], y: ArrayLike):
        pass

    @abstractmethod
    def predict(self, X: List[Notebook]) -> List[List[str]]:
        pass
