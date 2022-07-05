from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / 'data'

SOURCE_DATA = DATA_PATH / 'source-data'
EXPERIMENT_DATA = DATA_PATH / 'experiment-data'

TRAIN = 'train'

ANCESTORS = 'train_ancestors.csv'
ORDERS = 'train_orders.csv'
