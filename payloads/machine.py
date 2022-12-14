from .core import BasePayload
from enum import Enum


# noinspection PyPep8Naming
class MachinePayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo', 'executedBy', 'executedIn']

    class Status(Enum):
        WAITING = 0
        ACTIVE = 1
        FINISHED = 2

    class Type(Enum):
        RECEIVING = 'receiving_material'
        ORGANIZING = 'organizing_material'
        MACHINE = 'assembly'
        SHIPPING = 'shipping'
        CNC1 = 'cnc1'
        NESTING1 = 'nesting1'
        MANUALCUT1 = 'manualcut1'

    def __init__(self, **kwargs):
        super(MachinePayload, self).__init__(**kwargs)
        self.startTime = kwargs.get('startTime', '')
        self.finishTime = kwargs.get('finishTime', '')
        self.machineStatus = kwargs.get('machineStatus', 0)
        self.belongsTo = kwargs.get('belongsTo', '')
        self.image = kwargs.get('image', '')
        self.type = kwargs.get('type', 'Machine')
        self.executedIn = kwargs.get('executedIn', '')
        self.executedBy = kwargs.get('executedBy', '')
        self.machineType = kwargs.get('machineType', '')

    @property
    def startTime(self) -> str:
        return self._startTime

    @startTime.setter
    def startTime(self, startTime: str) -> None:
        self._startTime = startTime

    @property
    def finishTime(self) -> float:
        return self._finishTime

    @finishTime.setter
    def finishTime(self, finishTime: float) -> None:
        self._finishTime = finishTime

    @property
    def machineStatus(self) -> int:
        return self._machineStatus

    @machineStatus.setter
    def machineStatus(self, machineStatus: int) -> None:
        self._machineStatus = machineStatus

    @property
    def belongsTo(self) -> str:
        return self._belongsTo

    @belongsTo.setter
    def belongsTo(self, belongsTo: str) -> None:
        self._belongsTo = belongsTo

    @property
    def machineType(self) -> str:
        return self._machineType

    @machineType.setter
    def machineType(self, machineType: str) -> None:
        self._machineType = machineType

    @property
    def executedBy(self) -> str:
        return self._executedBy

    @executedBy.setter
    def executedBy(self, executedBy: str) -> None:
        self._executedBy = executedBy

    @property
    def executedIn(self) -> str:
        return self._executedIn

    @executedIn.setter
    def executedIn(self, executedIn: str) -> None:
        self._executedIn = executedIn
