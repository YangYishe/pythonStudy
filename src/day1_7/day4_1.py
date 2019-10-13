"""
输入一个正整数判断是不是素数。
"""
i1 = int(input('input a integer:'))
ic = int(i1 ** 0.5)
print('middle:%d' % ic)
flag = True
for ie in range(2, ic+1):
    if i1 % ie == 0:
        flag = False
        print('这不是素数,可被%d整除' % ie)
        break
if flag:
    print('这是素数')
