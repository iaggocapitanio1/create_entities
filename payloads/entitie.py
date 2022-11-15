from .core import BasePayload


class EntitiesPayload(BasePayload):

    def __init__(self, **kwargs):
        super(EntitiesPayload, self).__init__(**kwargs)
        self.email = kwargs.get('email', '')
        self.taxId = kwargs.get('taxId', '')

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def taxId(self) -> float:
        return self._taxId

    @taxId.setter
    def taxId(self, taxId: float) -> None:
        self._taxId = taxId
