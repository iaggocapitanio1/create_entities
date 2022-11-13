from pathlib import Path
from .parser import Parser

BASE_DIR = Path(__file__).resolve().parent.parent

settings = Parser()

settings.read('settings/settings.ini')
