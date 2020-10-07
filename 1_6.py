#Задача 6

a, b = int(input('Введите кол-во км для начала: ')), int(input('Введите сколько нужно пробежать: '))
i = 0
while True:
    i+=1
    print(str(i)+str('-й день'), round(a,2))
    a += a* 0.1
    if a > b:
        i+=1
        print(str(i)+str('-й день'), round(a,2))
        break
