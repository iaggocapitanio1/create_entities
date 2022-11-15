from .core import BasePayload

from enum import Enum


class PermissionPayload(BasePayload):
    class Actions(Enum):
        CREATE_READ_UPDATE_DELETE = 'CRUD'
        CREATE_READ_UPDATE = 'CRU'
        CREATE_READ = 'CR'
        READ = 'R'

    def __init__(self, **kwargs):
        super(PermissionPayload, self).__init__(**kwargs)
        self.type = kwargs.get('type', 'Permission')
        self.action = kwargs.get('action', '')
        self.hasOwner = kwargs.get('hasOwner', '')
        self.hasWorker = kwargs.get('hasWorker', '')

    @property
    def action(self) -> str:
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        self._action = action

    @property
    def hasOwner(self) -> str:
        return self._hasOwner

    @hasOwner.setter
    def hasOwner(self, hasOwner: str) -> None:
        self._hasOwner = hasOwner

    @property
    def hasWorker(self) -> str:
        return self._hasWorker

    @hasWorker.setter
    def hasWorker(self, hasWorker: str) -> None:
        self._hasWorker = hasWorker
