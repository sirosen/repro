from typing import Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def noop(f: Callable[P, R]) -> Callable[P, R]:
    return f


def foo(x: int) -> str:
    return str(x)


reveal_type(foo)
reveal_type(noop(foo))
