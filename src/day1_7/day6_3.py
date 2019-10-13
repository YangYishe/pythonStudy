"""
实现判断一个数是不是素数的函数。
"""


# same as day5_6.py
def is_prime(a):
    b = int(a ** 0.5)
    for i in range(2, b):
        if a % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(2, 101):
        if is_prime(i):
            print(i, end=',')
