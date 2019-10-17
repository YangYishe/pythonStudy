"""
从一段文字中提取出国内手机号码。
1+34578
3种方式来查询出来字符串中的全部手机号.
"""
import re

def main():
    try:
        with open('day12.txt','r',encoding='utf8') as f:
            s=f.read()
            # print(s)
            pat=re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
            mylist=re.findall(pat,s)
            print(mylist)
            print('---split---')
            myiter=re.finditer(pat,s)
            for temp in myiter:
                print(temp.group())
            print('---split---')
            m=pat.search(s)
            while m:
                print(m.group())
                m=pat.search(s,m.end())
    except FileNotFoundError:
        print('can not found files')
    pass


if __name__ == '__main__':
    main()