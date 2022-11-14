from .core import BasePayload


# noinspection PyPep8Naming
class PartPayload(BasePayload):
    RELATIONAL_PROPS = ['belongsTo']

    def __init__(self, **kwargs):
        super(PartPayload, self).__init__(**kwargs)
        self.type = kwargs.get('type', 'Part')
        self.partName = kwargs.get('partName', '')
        self.sort = kwargs.get('sort', '')
        self.material = kwargs.get('material', '')
        self.amount = kwargs.get('amount', -1)
        self.length = kwargs.get('length', -1)
        self.width = kwargs.get('width', -1)
        self.thickness = kwargs.get('thickness', -1)
        self.tag = kwargs.get("tag", -1)
        self.nestingFlag = kwargs.get("nestingFlag", False)
        self.cncFlag = kwargs.get("cncFlag", False)
        self.f2 = kwargs.get("f2", -1)
        self.f3 = kwargs.get("f3", -1)
        self.f4 = kwargs.get("f4", -1)
        self.f5 = kwargs.get("f5", -1)
        self.veio = kwargs.get("veio", "Y")
        self.orla2 = kwargs.get("orla2", False)
        self.orla3 = kwargs.get("orla3", False)
        self.orla4 = kwargs.get("orla4", False)
        self.orla5 = kwargs.get("orla5", False)
        self.observation = kwargs.get("observation", "")
        self.weight = kwargs.get("weight", -1)
        self.image = kwargs.get("image", "")
        self.belongsTo = kwargs.get("belongsTo", "")

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

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        self._weight = weight

    @property
    def observation(self) -> str:
        return self._observation

    @observation.setter
    def observation(self, observation: str) -> None:
        self._observation = observation

    @property
    def orla5(self) -> bool:
        return self._orla5

    @orla5.setter
    def orla5(self, orla5: bool) -> None:
        self._orla5 = orla5

    @property
    def orla4(self) -> bool:
        return self._orla4

    @orla4.setter
    def orla4(self, orla4: bool) -> None:
        self._orla4 = orla4

    @property
    def orla3(self) -> bool:
        return self._orla3

    @orla3.setter
    def orla3(self, orla3: bool) -> None:
        self._orla3 = orla3

    @property
    def orla2(self) -> bool:
        return self._orla2

    @orla2.setter
    def orla2(self, orla2: bool) -> None:
        self._orla2 = orla2

    @property
    def veio(self) -> str:
        return self._veio

    @veio.setter
    def veio(self, veio: str) -> None:
        self._veio = veio

    @property
    def f5(self) -> int:
        return self._f5

    @f5.setter
    def f5(self, f5: int) -> None:
        self._f5 = f5

    @property
    def f4(self) -> int:
        return self._f4

    @f4.setter
    def f4(self, f4: int) -> None:
        self._f4 = f4

    @property
    def f3(self) -> int:
        return self._f3

    @f3.setter
    def f3(self, f3: int) -> None:
        self._f3 = f3

    @property
    def f2(self) -> int:
        return self._f2

    @f2.setter
    def f2(self, f2: int) -> None:
        self._f2 = f2

    @property
    def cncFlag(self) -> bool:
        return self._cncFlag

    @cncFlag.setter
    def cncFlag(self, cncFlag: bool) -> None:
        self._cncFlag = cncFlag

    @property
    def nestingFlag(self) -> bool:
        return self._nestingFlag

    @nestingFlag.setter
    def nestingFlag(self, nestingFlag: bool) -> None:
        self._nestingFlag = nestingFlag

    @property
    def thickness(self) -> float:
        return self._thickness

    @thickness.setter
    def thickness(self, thickness: float) -> None:
        self._thickness = thickness

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width = width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount

    @property
    def partName(self) -> str:
        return self._partName

    @partName.setter
    def partName(self, partName: str) -> None:
        self._partName = partName

    @property
    def sort(self) -> str:
        return self._sort

    @sort.setter
    def sort(self, sort: str) -> None:
        self._sort = sort

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, material: str) -> None:
        self._material = material
