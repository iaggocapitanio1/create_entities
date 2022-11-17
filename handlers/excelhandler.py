from watchdog.events import FileSystemEvent
from .patternEventHandler import PatternEventHandler


class ExcelEventHandler(PatternEventHandler):

    def __init__(self, *args, **kwargs):
        super(ExcelEventHandler, self).__init__(*args, **kwargs)

    def on_created(self, event: FileSystemEvent):
        pass