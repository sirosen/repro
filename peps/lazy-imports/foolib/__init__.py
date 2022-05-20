SHOULD_FAIL = False

if SHOULD_FAIL:
    from .foo import Foo
    from .bar import Bar, BarWithFoo
else:
    from .bar import Bar, BarWithFoo
    from .foo import Foo
