from .path import validate_path as validate_path_func

def validate_path(method):
    def wrapper(self, value):
        