"""
定义一个类描述数字时钟。
"""
from time import sleep


class DigitalClock:

    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second >= 60:
            self._second %= 60
            self._minute += 1
        if self._minute >= 60:
            self._minute %= 60
            self._hour += 1
        if self._hour >= 24:
            self._hour %= 24

    def show(self):
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


def main():
    dc = DigitalClock(9, 3, 30)
    while True:
        sleep(1)
        dc.run()
        dc.show()


if __name__ == '__main__':
    main()
