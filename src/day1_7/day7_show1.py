str1 = r'\hello,world!'

print(str1.center(60, '*'))
print(str1.rjust(50, '+'))

str2 = '23dd42355'

print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())

str3=' afdsf '

print(str3.strip())

str4='sdfsdfds'

print('sdf' in str4)
print(str4[3])
print(str4[1:5])

num1,num2=10,13

print('{0}+{1}={2}'.format(num1,num2,num1+num2))
print(f'{num1}*{num2}={num1*num2}')