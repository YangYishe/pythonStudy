"""
self define test
"""
from abc import abstractclassmethod, ABCMeta
from random import randint


class Card(object, metaclass=ABCMeta):
    __slots__ = ("_typ", "_val")

    def __init__(self, typ, val):
        self._typ = typ
        self._val = val

    @abstractclassmethod
    def use(self, target):
        pass


class AttackCard(Card):

    def __init__(self, typ, val):
        super().__init__(typ, val)

    def use(self, target):
        target._hp -= self._val

    @classmethod
    def get_instance(cls):
        val = randint(1, 10)
        return cls(AttackCard.default_typ(), val)

    @staticmethod
    def default_typ():
        return 1

    def __str__(self):
        return f'atk{self._val}'


class HealCard(Card):
    def __init__(self, typ, val):
        super().__init__(typ, val)

    def use(self, target):
        target._hp += self._val

    @classmethod
    def get_instance(cls):
        val = randint(1, 10)
        return cls(HealCard.default_type(), val)

    @staticmethod
    def default_type():
        return 2

    def __str__(self):
        return f'heal{self._val}'


class Role:
    def __init__(self, hp):
        self._hp = hp


def main():
    typ = randint(1, 3)
    print(typ)
    if typ == 1:
        print(AttackCard.get_instance())
    else:
        print(HealCard.get_instance())
    pass


if __name__ == '__main__':
    main()
