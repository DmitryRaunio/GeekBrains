a = str(input('Введите число: '))
while True:
    b = a[1]
    for i in a:
        if b < i: b=i
    print(b)
    break