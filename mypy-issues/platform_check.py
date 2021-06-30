import os
import sys


def foo():
    if sys.platform == "win32":
        return 1
    return 0


def bar():
    if sys.platform != "win32":
        return 1
    return 0


def data_dir():
    if sys.platform == "win32":
        datadir = os.getenv("LOCALAPPDATA", os.getenv("APPDATA"))
        if not datadir:
            home = os.path.expanduser("~")
            datadir = os.path.join(home, "AppData", "Local")
        return os.path.join(datadir, "my-app")
    return os.path.expanduser("~/.my-app")
