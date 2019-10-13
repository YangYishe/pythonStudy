import sys

def resort1(num):
    return num%3

arr1=[1,2,3,6,8]

print(len(arr1))
print(sorted(arr1,key=resort1))

# 这种方法实际上生成的是一个矩阵
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 这种方法类似于Map
arr2 = [x-1 for x in arr1]
print(arr2)

print(sys.getsizeof(f))