from .bar import Bar


class BaseFoo:
    def __init__(self, bar: Bar):
        self.bar = bar


class Foo(BaseFoo):
    pass
