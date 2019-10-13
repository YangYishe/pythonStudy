"""
打印杨辉三角。
"""
def yhsj(n):
    arr1=[1,1]
    for i in range(n-1):
        arr2=[1]
        for j in range(i):
            arr2.append(arr1[j]+arr1[j+1])
        arr2.append(1)
        arr1=arr2
        yield arr1
    pass

def main():
    for i in yhsj(10):
        print(i)
    pass

if __name__ == '__main__':
    main()