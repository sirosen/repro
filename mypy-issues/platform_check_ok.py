import sys


def foo():
    if sys.platform == "win32":
        return 1
    else:
        return 0


def bar():
    if sys.platform != "win32":
        return 1
    else:
        return 0
