"""
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""


def is_prime(a):
    b = int(a ** 0.5)
    for i in range(2, b):
        if a % i == 0:
            return False
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i, end=',')
