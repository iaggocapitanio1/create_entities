from .core import BasePayload


# noinspection PyPep8Naming
class MachinePayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo']

    def __init__(self, **kwargs):
        super(MachinePayload, self).__init__(**kwargs)
        self.startTime = kwargs.get('startTime', '')
        self.finishTime = kwargs.get('finishTime', -1)
        self.machineStatus = kwargs.get('machineStatus', '')
        self.belongsTo = kwargs.get('belongsTo', '')
        self.image = kwargs.get('type', 'Machine')
        self.machineType = kwargs.get('type', 'Machine')
        self.executedIn = kwargs.get('executedIn', '')
        self.executedBy = kwargs.get('executedBy', '')

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
    def machineStatus(self) -> str:
        return self._machineStatus

    @machineStatus.setter
    def machineStatus(self, machineStatus: str) -> None:
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
    def executedBy(self) -> float:
        return self._executedBy

    @executedBy.setter
    def executedBy(self, executedBy: float) -> None:
        self._executedBy = executedBy

    @property
    def executedIn(self) -> str:
        return self._executedIn

    @executedIn.setter
    def executedIn(self, executedIn: str) -> None:
        self._executedIn = executedIn
