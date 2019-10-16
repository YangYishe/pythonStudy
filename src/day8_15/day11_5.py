"""
读JSON文件
"""

import json

def main():
    try:
        with open('data.json','r',encoding='utf8') as f:
            m=json.load(f)
            print(m['name'])
    except FileNotFoundError:
        print('file not found')

    pass


if __name__ == '__main__':
    main()