from .core import BasePayload


# noinspection PyPep8Naming
class BudgetPayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo']

    def __init__(self, **kwargs):
        super(BudgetPayload, self).__init__(**kwargs)
        self.name = kwargs.get('name', '')
        self.amount = kwargs.get('amount', -1)
        self.approvedDate = kwargs.get('approvedDate', '')
        self.belongsTo = kwargs.get('belongsTo', '')
        self.image = kwargs.get('image', '')

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

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        self._image = image
