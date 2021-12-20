x = 0
while x == 0:
    try:
        x = int(input('Введите число: '))
        print(x)
    except ValueError:
        print('Введите целое число')