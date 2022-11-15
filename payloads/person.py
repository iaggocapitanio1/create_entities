from .core import BasePayload


# noinspection PyPep8Naming
class PersonPayload(BasePayload):
    def __init__(self, **kwargs):
        super(PersonPayload, self).__init__(**kwargs)
        self.givenName = kwargs.get('givenName', '')
        self.familyName = kwargs.get('familyName', '')
        self.email = kwargs.get('email', '')
        self.image = kwargs.get('type', 'Machine')
        self.password = kwargs.get('type', 'Machine')
        self.ssnId = kwargs.get('ssnId', '')
        self.taxId = kwargs.get('taxId', '')
        self.active = kwargs.get('active', False)
    @property
    def givenName(self) -> str:
        return self._givenName

    @givenName.setter
    def givenName(self, givenName: str) -> None:
        self._givenName = givenName

    @property
    def familyName(self) -> str:
        return self._familyName

    @familyName.setter
    def familyName(self, familyName: str) -> None:
        self._familyName = familyName

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        self._password = password

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

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, active: bool) -> None:
        self._active = active