"""
拆分长字符串
窗前明月光，疑是地上霜。举头望明月，低头思故乡。
，。, .
"""

import re

def main():
    sentence='窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    arr=re.split(r'[，。, .]',sentence)
    for temp in arr:
        print(temp)

if __name__ == '__main__':
    main()