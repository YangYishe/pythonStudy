"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def throw_people(bf,fi=0,ti=8):
    if len(bf)<9:
        return bf
    throw_index=(fi+ti)%len(bf)
    bf.remove(bf[throw_index])
    return throw_index

def first_people(n):
    arr=[]
    for i in range(n):
        arr.append(i)
    return arr

def throw_many(arr,n):
    first_index=0
    for _ in range(n):
        first_index=throw_people(arr,first_index)
        print(arr)
    pass

def main():
    arr=first_people(30)
    throw_many(arr,15)
    print(f'final:{arr}')

    pass

if __name__ == '__main__':
    main()