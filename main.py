from typing import Any, List
import inspect

def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator
class A(object):
    def __init__(self, **kwargs):
        keys = kwargs.keys()
        for key in keys:
            setattr(self, key, property(fset=self.f_set(key, kwargs[key]), fget=self.f_get(key)))

    def get_all_properties(self) -> List[str]:
        return [prop[0] for prop in inspect.getmembers(self.__class__, lambda inst: isinstance(inst, property))]

    def f_set(self, key: str, value) -> None:
        setattr(self, key, value)
    @rename('joao')
    def f_get(self, key: str) -> Any:
        return getattr(self, key)


if __name__ == '__main__':
    a = A(name='john')
    print(a.name.fget)
    print(a.get_all_properties())
