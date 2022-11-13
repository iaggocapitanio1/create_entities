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
