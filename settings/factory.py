from .parser import Parser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

configer = Parser()

configer['NGSI-LD'] = {
    'CONTEXT': [
        "https://raw.githubusercontent.com/More-Collaborative-Laboratory/ww4zero/main/ww4zero.context.normalized.jsonld",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ],
    "URL": "http://localhost:1026/ngsi-ld/v1"
}

configer['HEADERS'] = {
    "Content-Type": "application/ld+json",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "Fiware-Service":  "woodwork40"
}
configer['DATA-FRAME_PANELS'] = {
    'COLUMNS': [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'SHEET': 6
}

configer['DATA-FRAME_COMPACT-PANELS'] = {
    'COLUMNS': [0, 2,  3,  4, 5, 6,  7,  8, 9,  10, 11, 12, 13, 14, 15],
    'SHEET': 9
}
configer['DATA-FRAME_ACCESSORIES'] = {
    'COLUMNS': [0, 2,  3,  4],
    'SHEET': 7
}
with open(BASE_DIR.joinpath('settings/settings.ini'), 'w') as conf:
    configer.write(conf)
