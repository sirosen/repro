import typing

from greeklib import Gamma


class Alpha(Gamma):
    x = 1


class Beta(Gamma):
    x = 2


def gen1() -> typing.Iterable[Alpha]:
    return [Alpha()]


def gen2() -> typing.Iterable[Beta]:
    return [Beta()]


def foo() -> None:
    for x in gen1():
        reveal_type(x)

    for x in gen2():
        reveal_type(x)
