from .person import PersonPayload
from enum import Enum


class WorkerPayload(PersonPayload):
    RELATIONAL_PROPS = ['hasPermission', 'hasOrganization']

    class Shifts(Enum):
        MORNING = 'Morning'
        AFTERNOON = 'Afternoon'
        NIGHT = 'Night'

    def __init__(self, **kwargs):
        super(WorkerPayload, self).__init__(**kwargs)
        self.id = kwargs.get('type', 'Worker')
        self.workerShift = kwargs.get('workerShift', '')
        self.workerImage = kwargs.get('workerImage', '')
        self.hasOrganization = kwargs.get('hasOrganization', '')
        self.hasPermission = kwargs.get('hasPermission', '')

    @property
    def workerShift(self) -> str:
        return self._workerShift

    @workerShift.setter
    def workerShift(self, workerShift: str) -> None:
        self._workerShift = workerShift

    @property
    def workerImage(self) -> str:
        return self._workerImage

    @workerImage.setter
    def workerImage(self, workerImage: str) -> None:
        self._workerImage = workerImage

    @property
    def hasPermission(self) -> str:
        return self._hasPermission

    @hasPermission.setter
    def hasPermission(self, hasPermission: str) -> None:
        self._hasPermission = hasPermission

    @property
    def hasOrganization(self) -> str:
        return self._hasOrganization

    @hasOrganization.setter
    def hasOrganization(self, hasOrganization: str) -> None:
        self._hasOrganization = hasOrganization