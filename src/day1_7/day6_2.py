"""
实现判断一个数是不是回文数的函数。
"""


def get_each_wei(a):
    arr = []
    while True:
        arr.append(a % 10)
        a //= 10
        if a == 0:
            break
    return arr


def is_hw(a):
    arr = get_each_wei(a)
    for i in range(arr.__len__() // 2 + 1):
        if arr[i] != arr[arr.__len__() - i - 1]:
            return False

    return True


# if __name__ == '__main__':
#     a1 = int(input('a='))
#     print(is_hw(a1))
