SHOULD_FAIL = True

if SHOULD_FAIL:
    from .foo import BaseFoo, Foo
    from .bar import Bar, BarWithFoo
else:
    from .bar import Bar, BarWithFoo
    from .foo import BaseFoo, Foo
