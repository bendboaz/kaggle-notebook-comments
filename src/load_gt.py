import json
import os
from typing import Tuple, List, Mapping

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import ExperimentSettings
from src.constants import ANCESTOR_ID, CELL_ORDER, Y, ID
from src.paths import TRAIN, ORDERS, ANCESTORS, SOURCE_DATA, EXPERIMENT_DATA
from src.load_notebooks import read_notebook_file
from src.types.notebook import Notebook


def load_gt(config: ExperimentSettings) -> Mapping[str, Tuple[List[Notebook], pd.DataFrame]]:
    """
    Load full GT and perform train-test splitting.
    :param config: ExperimentSettings object.
    :return: A dictionary containing entries for train and test,
        each with a list of Notebook objects and a dataframe containing labels + metadata.
    """
    gt_notebooks, gt_metadata = load_raw_gt()
    partitions_dict = split_gt(config, gt_notebooks, gt_metadata)
    return partitions_dict


def load_raw_gt() -> Tuple[List[Notebook], pd.DataFrame]:
    """
    Loads the full GT, including notebook data, correct orders and ancestry metadata.
    :return:
        - notebooks: (list[Notebook]) List of loaded notebook objects
        - structured_data: (DataFrame) DataFrame with the following columns:
            - notebook_id: (str)
            - y: list(str) List of <it>cell_id</it>s representing the correct markdown order.
            - ancestor_id: (str) Identifier for the notebook family.
            - parent_id: (str) Direct fork parent of the notebook.
    """
    partition_dir = SOURCE_DATA / TRAIN
    notebooks = [read_notebook_file(partition_dir / filename) for filename in os.listdir(str(partition_dir))]

    structured_data = load_gt_metadata()

    return notebooks, structured_data


def load_gt_metadata() -> pd.DataFrame:
    orders_df = pd.read_csv(SOURCE_DATA / ORDERS, index_col=ID).rename(columns={CELL_ORDER: Y})
    ancestors_df = pd.read_csv(SOURCE_DATA / ANCESTORS, index_col=ID)
    structured_data = orders_df.merge(ancestors_df, left_index=True, right_index=True)
    return structured_data


def create_split_data(config: ExperimentSettings) -> Mapping[str, List[str]]:
    structured_data = load_gt_metadata()
    ancestries = structured_data[ANCESTOR_ID]
    train_ancestries, val_ancestries = train_test_split(ancestries, test_size=config.gt.train_part)
    return {
        'train': structured_data[structured_data[ANCESTOR_ID].isin(train_ancestries)].index.tolist(),
        'val': structured_data[structured_data[ANCESTOR_ID].isin(val_ancestries)].index.tolist(),
    }


def get_split_data(config: ExperimentSettings):
    experiment_name = config.experiment_name
    experiment_path = EXPERIMENT_DATA / experiment_name

    if config.gt.force_split or not experiment_path.is_dir():
        split_data = create_split_data(config)
        experiment_path.mkdir(parents=True, exist_ok=True)
        with open(experiment_path / 'split.json', 'w+') as f:
            json.dump(split_data, f)

    else:
        with open(experiment_path / 'split.json', 'r') as f:
            split_data = json.load(f)

    return split_data


def split_gt(config: ExperimentSettings, gt_notebooks: List[Notebook], gt_metadata: pd.DataFrame) \
        -> Mapping[str, Tuple[List[Notebook], pd.DataFrame]]:
    split_data = get_split_data(config)
    partitions = ['train', 'dev']
    notebooks = {
        partition: list(filter(lambda nb: nb.notebook_id in split_data[partition], gt_notebooks))
        for partition in partitions
    }

    metadata = {
        partition: gt_metadata[gt_metadata.index.isin(split_data[partition])]
        for partition in partitions
    }

    return {
        partition: (notebooks[partition], metadata[partition])
        for partition in partitions
    }
