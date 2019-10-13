"""
打印如下所示的三角形图案。
"""
for i1 in range(1, 6):
    for i2 in range(1, i1 + 1):
        print('*', end='')
    print('')

for i1 in range(1, 6):
    for i2 in range(1, 6):
        if i2 + i1 <= 5:
            print(' ', end='')
        else:
            print('*', end='')
    print('')

for i1 in range(1, 6):
    for i2 in range(1, i1 + 5):
        if i2 <= 5 - i1:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
