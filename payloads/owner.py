from .person import PersonPayload


class OwnerPayload(PersonPayload):
    RELATIONAL_PROPS = ['hasPermission', 'belongsTo']

    def __init__(self, **kwargs):
        super(OwnerPayload, self).__init__(**kwargs)
        self.type = kwargs.get('type', 'Owner')
        self.legalName = kwargs.get('legalName', '')
        self.ownerClass = kwargs.get('ownerClass', '')
        self.ownerType = kwargs.get('ownerType', False)
        self.address = kwargs.get('address', '')
        self.obs = kwargs.get('obs', '')
        self.telephone = kwargs.get('telephone', '')
        self.hasPermission = kwargs.get('hasPermission', '')
        self.belongsTo = kwargs.get('belongsTo', '')

    @property
    def legalName(self) -> str:
        return self._legalName

    @legalName.setter
    def legalName(self, legalName: str) -> None:
        self._legalName = legalName

    @property
    def ownerClass(self) -> bool:
        return self._ownerClass

    @ownerClass.setter
    def ownerClass(self, ownerClass: bool) -> None:
        self._ownerClass = ownerClass

    @property
    def ownerType(self) -> bool:
        return self._ownerType

    @ownerType.setter
    def ownerType(self, ownerType: bool) -> None:
        self._ownerType = ownerType

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
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        self._image = image

    @property
    def obs(self) -> str:
        return self._obs

    @obs.setter
    def obs(self, obs: str) -> None:
        self._obs = obs

    @property
    def hasPermission(self) -> str:
        return self._hasPermission

    @hasPermission.setter
    def hasPermission(self, hasPermission: str) -> None:
        self._hasPermission = hasPermission

    @property
    def belongsTo(self) -> str:
        return self._belongsTo

    @belongsTo.setter
    def belongsTo(self, belongsTo: str) -> None:
        self._belongsTo = belongsTo
