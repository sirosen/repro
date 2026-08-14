from unittest import mock


class Adder:
    def plus(self, a: int, b: int) -> int:
        return a + b


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

    assert snek.plus(1, 2) == 3  # wat
