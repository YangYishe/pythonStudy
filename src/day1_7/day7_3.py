"""
设计一个函数返回给定文件名的后缀名。
"""

def get_suffix(file_name):
    i=file_name.rfind('.')
    return file_name[i+1:]
    pass

def main():
    print(get_suffix('day.7_3.py'))

    pass

if __name__ == '__main__':
    main()