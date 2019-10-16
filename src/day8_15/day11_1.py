"""
file read
"""
from time import sleep


def main():
    # 此处使用绝对路径
    # f = None
    try:
        # utf8和utf-8均可
        # f = open('C:/Users/Administrator/Desktop/test.txt', 'r', encoding='utf8')
        with open('C:/Users/Administrator/Desktop/test.txt', 'r', encoding='utf8') as f:
            print(f.read())

            for line in f:
                print(line, end='')
                sleep(0.5)
            f.close()

        with open('C:/Users/Administrator/Desktop/test.txt',mode='r') as f:
            for line in f:
                print(line, end='')
                sleep(0.5)


    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('指定了不存在的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    # finally:
    #     if f:
    #         f.close()

    pass


if __name__ == '__main__':
    main()
