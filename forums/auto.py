from core import (
    banner,
    color,
    symbol,
    clear,
    highlight,
    info_highlight,
    error_highlight,
    css
)

from api.extract import *
import json
import sys
import threading 
try:
    from urllib.request import urlopen
except:
    print(f"{color.redbg}Please use python version >3.0.{color.reset} {color.bold}Otherwise write issue by using {color.greenbg}official github{color.reset}{color.bold} repo to get better support.{color.reset}")
    sys.exit(0)


class config:
    focmint = "./.db/forums.json"


def get_db():
    with open(config.focmint,"r") as f:
        return json.loads(f.read())