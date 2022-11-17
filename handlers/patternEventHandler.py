from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
from typing import Union


class PatternEventHandler(PatternMatchingEventHandler):

    def __init__(self, *args, **kwargs):
        super(PatternEventHandler, self).__init__(*args, **kwargs)

    @property
    def target_path(self) -> Path:
        return self._path

    @target_path.setter
    def target_path(self, path: Union[Path, str]) -> str:
        if isinstance(path, str):
            path = Path(path).resolve()
        self._path = path
