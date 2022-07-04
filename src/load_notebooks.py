import json
from pathlib import Path
from typing import Union, List, Mapping

from src.types.notebook import Notebook, Cell


def read_notebook_file(path: Union[str, Path]) -> Notebook:
    path = Path(path)

    if not path.is_file():
        raise LookupError(f'No file found in path {path}')

    with open(path, 'r') as f:
        notebook_dict = json.load(f)

    noteobok_id = path.name.split('.')[0]

    code_cells = list(filter(lambda cell_id: notebook_dict['cell_type'] == 'code', notebook_dict['source']))
    markdown_cells = list(filter(lambda cell_id: notebook_dict['cell_type'] == 'markdown', notebook_dict['source']))

    cell_contents = notebook_dict['source']

    code_cells = load_cells(cell_contents, code_cells)
    md_cells = load_cells(cell_contents, markdown_cells)

    notebook = Notebook(
        noteobok_id,
        code_cells,
        md_cells,
    )

    return notebook


def load_cells(cell_contents: Mapping[str, str], cell_ids: List[str]) -> List[Cell]:
    cell_ids = [Cell(cell_id, cell_contents[cell_id]) for cell_id in cell_ids]
    return cell_ids
