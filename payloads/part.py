from .core import BasePayload


# noinspection PyPep8Naming
class PartPayload(BasePayload):

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

    @property
    def f5(self) -> int:
        return self._f5

    @f5.setter
    def f2(self, f5) -> None:
        self._f5 = f5

    @property
    def f4(self) -> int:
        return self._f4

    @f4.setter
    def f4(self, f4) -> None:
        self._f4 = f4

    @property
    def f3(self) -> int:
        return self._f3

    @f3.setter
    def f3(self, f3) -> None:
        self._f3 = f3

    @property
    def f2(self) -> int:
        return self._f2

    @f2.setter
    def f2(self, f2) -> None:
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
