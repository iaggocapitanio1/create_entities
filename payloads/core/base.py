from typing import List, Dict, Any
from settings import settings
import inspect


def parse_string_to_list(string_list: str) -> list:
    import ast
    return ast.literal_eval(string_list)


class BasePayload(object):
    PROPS_TO_EXCLUDE = ['context', 'headers', 'url', 'id', 'type']
    RELATIONAL_PROPS = []

    def __init__(self, **kwargs) -> None:
        self.context = kwargs.get('context', settings.get('NGSI-LD', 'context'))
        self.headers = kwargs.get('headers', settings.sections_dict['HEADERS'])
        self.url = kwargs.get('url', settings.get('NGSI-LD', 'url'))
        self.type = kwargs.get('type', 'Part')
        self.id = kwargs.get('id', None)

    def validate_props(self, props: list) -> list:
        if not all(prop in self.get_all_properties() for prop in props) and len(props)!= 0:
            raise ValueError('PROPS ARE BAD IMPLEMENTED!')
        return props

    def get_props_to_exclude(self):
        return self.validate_props(props=self.PROPS_TO_EXCLUDE)

    def get_relational_props(self):
        return self.validate_props(props=self.RELATIONAL_PROPS)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, identifier) -> None:
        self._id = identifier

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, _type) -> None:
        self._type = _type

    @property
    def context(self) -> List[str]:
        return self._context

    @context.setter
    def context(self, context: List[str]) -> None:
        if isinstance(context, str):
            context = parse_string_to_list(string_list=context)
        self._context = context

    @property
    def headers(self) -> Dict[str, str]:
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, str]) -> None:
        self._headers = headers

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    def get_all_properties(self) -> List[str]:
        return [prop[0] for prop in inspect.getmembers(self.__class__, lambda inst: isinstance(inst, property))]

    def clean_properties(self) -> List[str]:
        props = self.get_all_properties()
        for removable in self.get_props_to_exclude() + self.get_relational_props():
            props.remove(removable)
        return props

    @staticmethod
    def create_field(_type: str, value: Any) -> Dict[str, Any]:
        return dict(type=_type, value=value)

    def body(self) -> dict:
        payload_body = dict(id=self.id, type=self.type)
        for prop in self.clean_properties():
            payload_body[prop] = self.create_field(_type='Property', value=getattr(self, prop))
        payload_body["@context"] = self.context
        for prop in self.get_relational_props():
            payload_body[prop] = self.create_field(_type='Relationship', value=getattr(self, prop))
        return payload_body
