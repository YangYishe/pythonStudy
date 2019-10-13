"""
设计一个函数返回传入的列表中最大和第二大的元素的值。
"""

def findMax2(arr):
    return sorted(arr)[len(arr)-2:len(arr)]

def main():
    print(findMax2([3,5,2,456,22,66,24]))
    pass

if __name__ == '__main__':
    main()