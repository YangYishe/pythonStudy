"""
计算指定的年月日是这一年的第几天。
"""

import src.day1_7.day2_3 as day2_3

def get_day_of_year(sd):
    y=int(sd[0:4])
    m=int(sd[5:7])
    d=int(sd[8:10])

    is_run=day2_3.isRun(y)
    month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

    days_sum=0
    for i in range(m):
        days_sum+=month_days[i]
    if is_run:
        days_sum+=1
    days_sum+=d

    return days_sum

def main():
    sd=input('today is :')
    print(get_day_of_year(sd))

if __name__ == '__main__':
    main()