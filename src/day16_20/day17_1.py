items1=list(map(lambda x:x**2,filter(lambda x:x%2,range(1,10))))
items2=[x**2 for x in range(1,10) if x%2]

print(items1)
print(items2)

items3=filter(lambda x:x%3==2,range(1,20))
while True:
    try:
        print(next(items3))
    except StopIteration:
        break