"""
奥特曼打小怪兽。
"""

from abc import ABCMeta, abstractclassmethod
from random import randint, randrange
from time import sleep


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ("_name", "_hp")

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractclassmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    _slots_ = ("_name", "_hp", "_mp")

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        """
        普通攻击
        :param other: 对手
        :return:
        """
        other._hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技
        :param other: 对手
        :return: 是否施放成功
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other._hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other._hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值:%d\n' % self._hp + \
               '魔法值:%d\n' % self._mp


class Monster(Fighter):
    __slots__ = ("_name", "_hp")

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值:%d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster._hp > 0:
            return True

    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end=';')


def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('火山', 250)
    m2 = Monster('海啸', 500)
    m3 = Monster('地震', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('===第%02d回合===' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print(f'{u.name}使用普通攻击打了{m.name}')
            u.attack(m)
            print(f'{u.name}魔法值回复了{u.resume()}点')
        elif skill <= 9:
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击')
            else:
                print(f'{u.name}使用魔法攻击失败')
        else:
            if u.huge_attack(m):
                print(f'{u.name}使用了终极必杀技虐杀了{m.name}')
            else:
                print(f'{u.name}使用了普通攻击打了{m.name}')
                print(f'{u.name}魔法值回复了{u.resume()}点')

        if m.alive:
            print(f'{m.name}回击了{u.name}')
            m.attack(u)
        display_info(u, ms)
        sleep(1)
        fight_round += 1

    print('战斗结束')
    if u.alive:
        print('奥德曼获得了胜利')
    else:
        print('小怪兽获得了胜利')


if __name__ == '__main__':
    main()
