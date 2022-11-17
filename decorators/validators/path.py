from validators import validate_path as validator
import functools


def validate_path(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        print('bora')
        if len(args) > 1:
            self = args[0]
            path = args[1]
            print(path)
            return method(self, validator(path=path))
        elif len(args) == 0:
            path = kwargs.get('path')
            return method(validator(path=path))
        else:
            path = args[0]
            return method(validator(path=path))
    return wrapper