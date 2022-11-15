from .entitie import EntitiesPayload


class OrganizationPayload(EntitiesPayload):

    def __init__(self, **kwargs):
        super(OrganizationPayload, self).__init__(**kwargs)
        self.legalName = kwargs.get('legalName', '')
        self.caeId = kwargs.get('caeId', '')
        self.address = kwargs.get('address', '')
        self.telephone = kwargs.get('telephone', '')
        self.location = kwargs.get('location', '')

    @property
    def legalName(self) -> str:
        return self._legalName

    @legalName.setter
    def legalName(self, legalName: str) -> None:
        self._legalName = legalName

    @property
    def caeId(self) -> str:
        return self._caeId

    @caeId.setter
    def caeId(self, caeId: str) -> None:
        self._caeId = caeId

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        self._address = address

    @property
    def telephone(self) -> str:
        return self._telephone

    @telephone.setter
    def telephone(self, telephone: str) -> None:
        self._telephone = telephone

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, location: str) -> None:
        self._location = location
