import json
from collections import defaultdict
from pathlib import Path
from typing import Union, List, Mapping, Any

from src.constants import CELL_TYPE, MARKDOWN, CODE, SOURCE
from src.types.notebook import Notebook, Cell


def read_notebook_file(path: Union[str, Path]) -> Notebook:
    path = Path(path)

    if not path.is_file():
        raise LookupError(f'No file found in path {path}')

    with open(path, 'r') as f:
        notebook_dict = json.load(f)

    notebook_id = get_notebook_id(path)

    type_to_cells = get_cell_type_mapping(notebook_dict)

    cell_contents = notebook_dict[SOURCE]

    code_cells = load_cells(cell_contents, type_to_cells[CODE])
    md_cells = load_cells(cell_contents, type_to_cells[MARKDOWN])

    notebook = Notebook(
        notebook_id,
        code_cells,
        md_cells,
    )

    return notebook


def get_notebook_id(path):
    return path.name.split('.')[0]


def get_cell_type_mapping(notebook_dict: Mapping[str, Any]) -> Mapping[str, List[str]]:
    type_to_cells = defaultdict(list)
    for cell_id, cell_type in notebook_dict[CELL_TYPE].items():
        type_to_cells[cell_type].append(cell_id)
    return type_to_cells


def load_cells(cell_contents: Mapping[str, str], cell_ids: List[str]) -> List[Cell]:
    cell_ids = [Cell(cell_id, cell_contents[cell_id]) for cell_id in cell_ids]
    return cell_ids
