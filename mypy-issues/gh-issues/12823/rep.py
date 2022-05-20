from __future__ import annotations


class Cat:
    pass


class Dog:
    pass


class MyClass:
    def __init__(self) -> None:
        self.pet: Dog | Cat | None = None

    def get_pet(self) -> Dog | Cat | None:
        if input() == 'yes':
            self.pet = Cat()
        else:
            self.pet = Dog()

        return self.pet
