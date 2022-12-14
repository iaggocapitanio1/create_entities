from .core import BasePayload


class EntitiesPayload(BasePayload):

    def __init__(self, **kwargs):
        super(EntitiesPayload, self).__init__(**kwargs)
        self.email = kwargs.get('email', '')
        self.taxId = kwargs.get('taxId', '')
        self.ssnId = kwargs.get('ssnId', '')

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

    @property
    def ssnId(self) -> str:
        return self._ssnId

    @ssnId.setter
    def ssnId(self, ssnId: str) -> None:
        self._ssnId = ssnId
