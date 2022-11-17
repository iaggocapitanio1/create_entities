from watchdog.events import PatternMatchingEventHandler, FileSystemEvent


class ExcelEventHandler(PatternMatchingEventHandler):

    def __init__(self, *args, **kwargs):
        super(ExcelEventHandler, self).__init__(*args, **kwargs)

