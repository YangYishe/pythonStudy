y=int(input('year='))
b1=y%4==0
b2=y%100==0 and y%400!=0
b=b1 and not b2
print('%s是闰年'%(b))