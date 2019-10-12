"""
写一个程序判断输入的正整数是不是回文素数。
"""
# 此处使用相对路径会报错
from src.day1_15.day6_2 import is_hw
from src.day1_15.day6_3 import is_prime

if __name__ == '__main__':
    for i in range(2, 1001):
        if is_hw(i) and is_prime(i):
            print(i)
