from ..foo import Foo


class BarWithFoo:
    def __init__(self, foo: Foo):
        self.foo = foo
