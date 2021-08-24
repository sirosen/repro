import typing


@typing.overload
def foo(x: "typing.Literal[True]") -> int:
    ...


@typing.overload
def foo(x: "typing.Literal[False]") -> str:
    ...


def foo(x: bool):
    """a func"""
    if x:
        return 1
    return "foo"
