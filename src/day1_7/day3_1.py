'''
1inch=2.54cm
'''
len=float(input('length num:'))
uni=input('unit(inch or cm):')
if uni=='inch' or uni=='英寸':
    print('=%fcm'%(len*2.54))
elif uni=='cm' or uni=='厘米':
    print('=%finch'%(len/2.54))
else:
    print('ilegal')