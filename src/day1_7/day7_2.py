"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random

def createYzm(n):
    s1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    s2=''
    for _ in range(n):
        s2+=s1[random.randint(0,len(s1))]
    return s2

def main():
    print(createYzm(4))

if __name__ == '__main__':
    main()