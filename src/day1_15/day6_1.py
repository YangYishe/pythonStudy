"""
实现计算求最大公约数和最小公倍数的函数。
"""


def max_gy(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        else:
            a = b
            b = c


def min_gb(a, b):
    return a * b / max_gy(a, b)


if __name__ == '__main__':
    a1 = int(input('a='))
    b1 = int(input('b='))

    print('max_gy=%d,min_gb=%d' % (max_gy(a1, b1), min_gb(a1, b1)))
