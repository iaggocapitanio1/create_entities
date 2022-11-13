from configparser import ConfigParser


class Parser(ConfigParser):

    def __init__(self, *args, **kwargs):
        super(Parser, self).__init__(*args, **kwargs)

    @property
    def sections_dict(self) -> dict:
        return self._sections


