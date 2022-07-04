from dataclasses import dataclass
from typing import List


@dataclass
class Cell:
    cell_id: str
    cell_content: str


@dataclass
class Notebook:
    notebook_id: str
    code_cells: List[Cell]
    md_cells: List[Cell]
