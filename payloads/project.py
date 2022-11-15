from .core import BasePayload


class ProjectPayload(BasePayload):
    RELATIONAL_PROPS = ['expedition', 'assemblyBy', 'orderBy', 'producedBy']

    def __init__(self, **kwargs):
        super(ProjectPayload, self).__init__(**kwargs)
        self.type = kwargs.get('type', 'Project')
        self.name = kwargs.get('name', '')
        self.category = kwargs.get('category', '')
        self.status = kwargs.get('status', '')
        self.producedBy = kwargs.get('producedBy', '')
        self.orderBy = kwargs.get('orderBy', '')
        self.assemblyBy = kwargs.get('assemblyBy', '')
        self.image = kwargs.get('image', '')
        self.expedition = kwargs.get('expedition', '')

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        self._category = category

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        self._status = status

    @property
    def producedBy(self) -> str:
        return self._producedBy

    @producedBy.setter
    def producedBy(self, producedBy: str) -> None:
        self._producedBy = producedBy

    @property
    def orderBy(self) -> str:
        return self._orderBy

    @orderBy.setter
    def orderBy(self, orderBy: str) -> None:
        self._orderBy = orderBy

    @property
    def assemblyBy(self) -> str:
        return self._assemblyBy

    @assemblyBy.setter
    def assemblyBy(self, assemblyBy: str) -> None:
        self._assemblyBy = assemblyBy

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        self._image = image

    @property
    def expedition(self) -> str:
        return self._expedition

    @expedition.setter
    def expedition(self, expedition: str) -> None:
        self._expedition = expedition

