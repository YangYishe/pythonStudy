"""
找出10000以内的完美数。

说明：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。
"""
import math

#It's not a good method.
#when num is big,it will waste too much time.
def isPerfect (a):
    _arr=[]
    for i in range(1,a):
        if a%i==0:
            _arr.append(i)

    if math.fsum(_arr)==a:
        return True
    else:
        return False

for i in range(1,10000):
    if isPerfect(i):
        print(i)

