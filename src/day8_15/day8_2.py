"""
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, x, y):
        self._x += x
        self._y += y

    def distance_between(self, other_point):
        return ((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2) ** 0.5

    def desc(self):
        return '{x:%f,y:%f}' % (self._x, self._y)


def main():
    p1 = Point(2, 4)
    p2 = Point(3, 8)
    p1.move(5, -10)
    print(p1.desc())
    print(p2.desc())
    print(f'distance:{p1.distance_between(p2)}')
    pass


if __name__ == '__main__':
    main()
