from pathlib import Path
from typing import Union


def validate_path(path: Union[Path, str]) -> Union[Path, str]:
    """
    Validate the type of path
    :param path: the target path to be validated.
    :return: path
    """
    if isinstance(path, str):
        path = Path(path).resolve()
    if isinstance(path, Path):
        return path
    raise ValueError(f'The path ({path}) is not an instance of str or pathlib.Path!')
