import typing as t

from click import Command


T = t.TypeVar("T")
_AnyCallable: t.TypeAlias = t.Callable[..., t.Any]
_Decorator: t.TypeAlias = t.Callable[[T], T]
FC = t.TypeVar("FC", bound=t.Union[_AnyCallable, Command])


def option() -> _Decorator[FC]:
    def decorator(f: FC) -> FC:
        return f

    return decorator


FC2: t.TypeAlias = t.Union[_AnyCallable, Command]
FC2_Decorator: t.TypeAlias = t.Callable[[FC2], FC2]


def option2() -> FC2_Decorator:
    def decorator(f: FC) -> FC:
        return f

    return decorator


def foo() -> None:
    pass


reveal_type(option)
reveal_type(option2)
foo = option()(foo)
foo2 = option2()(foo)
