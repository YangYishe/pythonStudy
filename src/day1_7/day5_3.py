"""
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""
from random import randint

winCount = 0
loseCount = 0
for i in range(100):
    print('第%d次' % i)
    first = randint(1, 6) + randint(1, 6)
    if first == 7 or first == 1:
        print('you win!first:%d' % first)
        winCount += 1
    elif first == 2 or first == 3 or first == 12:
        print('you lose!first:%d' % first)
        loseCount += 1
    else:
        while True:
            newPoint = randint(1, 6) + randint(1, 6)
            if newPoint == 7:
                print('you lose!first:%d,then:%d' % (first, newPoint))
                loseCount += 1
                break
            elif newPoint == first:
                print('you win!first:%d,then:%d' % (first, newPoint))
                winCount += 1
                break
print('you win %d times,lose %d times!' % (winCount, loseCount))
