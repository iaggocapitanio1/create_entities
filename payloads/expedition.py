from .core import BasePayload


# noinspection PyPep8Naming
class ExpeditionPayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo']

    def __init__(self, **kwargs):
        super(ExpeditionPayload, self).__init__(**kwargs)
        self.expeditionTime = kwargs.get('expeditionTime', '')
        self.deliveryFlag = kwargs.get('deliveryFlag', False)
        self.approvedDate = kwargs.get('approvedDate', '')
        self.belongsTo = kwargs.get('belongsTo', '')
        self.image = kwargs.get('type', 'Expedition')

    @property
    def expeditionTime(self) -> str:
        return self._expeditionTime

    @expeditionTime.setter
    def expeditionTime(self, expeditionTime: str) -> None:
        self._expeditionTime = expeditionTime

    @property
    def deliveryFlag(self) -> bool:
        return self._deliveryFlag

    @deliveryFlag.setter
    def deliveryFlag(self, deliveryFlag: bool) -> None:
        self._deliveryFlag = deliveryFlag

    @property
    def approvedDate(self) -> str:
        return self._approvedDate

    @approvedDate.setter
    def approvedDate(self, approvedDate: str) -> None:
        self._approvedDate = approvedDate

    @property
    def belongsTo(self) -> str:
        return self._belongsTo

    @belongsTo.setter
    def belongsTo(self, belongsTo: str) -> None:
        self._belongsTo = belongsTo
