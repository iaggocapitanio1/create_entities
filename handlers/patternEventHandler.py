from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
from typing import Union
from decorators import validate_path
import inspect


class PatternEventHandler(PatternMatchingEventHandler):

    def __init__(self, *args, **kwargs):
        super(PatternEventHandler, self).__init__(*args, **kwargs)
        self.target_path = kwargs.get('target_path', '')

    @property
    def target_path(self) -> Path:
        return self._path

    @target_path.setter
    @validate_path
    def target_path(self, path: Union[Path, str]) -> None:
        self._path = path

    def get_all_properties(self):
        return [prop[0] for prop in inspect.getmembers(self.__class__, lambda inst: isinstance(inst, property))]
