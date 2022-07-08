from operator import attrgetter
from typing import List

from numpy.typing import ArrayLike

from src.models.base_model import BaseNotebooksModel
from src.types.notebook import Notebook


class TransparentNotebooksModel(BaseNotebooksModel):
    def fit(self, X: List[Notebook], y: ArrayLike):
        return self

    def predict(self, X: List[Notebook]) -> List[List[str]]:
        return [list(map(attrgetter('cell_id'), nb.md_cells)) for nb in X]
