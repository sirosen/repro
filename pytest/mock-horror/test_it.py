from unittest import mock


class Adder:
    def plus(self, a: int, b: int) -> int:
        return a + b

    def double(self, a: int) -> int:
        return a + a


def test_patchy_stuff(monkeypatch):
    snek = Adder()
    with mock.patch.object(Adder, "plus", return_value=0):
        # ok
        assert snek.plus(1, 2) == 0

        # why u do this?
        monkeypatch.setattr(Adder, "plus", lambda *args: 1)
        assert snek.plus(3, 4) == 1


def test_abyssal_horror():
    snek = Adder()

    assert snek.plus(1, 2) == 0  # wat


def test_the_horror_continues(monkeypatch):
    snek = Adder()

    with monkeypatch.context() as mp_context:
        with mock.patch.object(Adder, "double", return_value=2):
            assert snek.double(2) == 2

            # uh-oh! it can happen here too!
            mp_context.setattr(Adder, "double", lambda *args: 1)
            assert snek.double(3) == 1

        # you expected this, right?
        assert snek.double(4) == 8

    assert snek.double(5) == 2  # wat
