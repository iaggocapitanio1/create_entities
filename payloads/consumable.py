from .core import BasePayload


# noinspection PyPep8Naming
class ConsumablePayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo']

    def __init__(self, **kwargs):
        super(ConsumablePayload, self).__init__(**kwargs)
        self.name = kwargs.get('name', '')
        self.amount = kwargs.get('amount', -1)
        self.status = kwargs.get('status', '')
        self.belongsTo = kwargs.get('belongsTo', '')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, amount: float) -> None:
        self._amount = amount

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        self._status = status

    @property
    def belongsTo(self) -> str:
        return self._belongsTo

    @belongsTo.setter
    def belongsTo(self, belongsTo: str) -> None:
        self._belongsTo = belongsTo

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        self._image = image
