"""
输入两个正整数，计算它们的最大公约数和最小公倍数。
"""
a = int(input('a='))
b = int(input('b='))
if a > b:
    imax = a
    imin = b
elif a < b:
    imax = b
    imin = a
else:
    print('最大公约数和最小公倍数均为%d' % a)

while a != b:
    c = imax % imin
    if c == 0:
        print('最大公约数:%d,最小公倍数:%d.' % (imin, a*b/imin))
        break
    else:
        imax = imin
        imin = c
