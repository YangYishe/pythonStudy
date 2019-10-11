"""
输入三条边长，如果能构成三角形就计算周长和面积。
a,b,c
海伦公式:
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
"""

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    print('this is a triangle!')
    print('周长为%f'%(a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print('area=%f' % area)
else:
    print('this is not a triangle!')