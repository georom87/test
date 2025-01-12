first = int(input('Число: '))
second = int(input('Число: '))
therd = int(input('Число: '))

if first==second==therd:
    print(3)
elif first==second or second==therd or therd==first:
    print(2)
else:
    print(0)
