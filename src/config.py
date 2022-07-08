from typing import Optional, Any

from pydantic import BaseSettings, Field
from pydantic.typing import StrPath


env_file_sentinel = str(object())


class GTConfig(BaseSettings):
    train_part: float
    force_split: bool = Field(default=False)


class ExperimentSettings(BaseSettings):
    gt: GTConfig
    experiment_name: str
    random_state: int = -1

    class Config:
        env_prefix = 'KAGGLE_NOTEBOOKS_'
        env_nested_delimiter = '__'

    def __init__(self,
                 _env_file: Optional[StrPath] = env_file_sentinel,
                 _env_file_encoding: Optional[str] = None,
                 _env_nested_delimiter: Optional[str] = None,
                 _secrets_dir: Optional[StrPath] = None,
                 **values: Any):
        super(ExperimentSettings, self).__init__(_env_file, _env_file_encoding, _env_nested_delimiter, _secrets_dir,
                                                 **values)
