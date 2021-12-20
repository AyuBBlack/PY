first_numb = 0
while first_numb == 0:
    try:
        first_numb = int(input('Введите первое число: '))
        second_numb = int(input('Введите второе число: '))

        def summa(c, d):
            return c + d
    except ValueError:
        print('Введите целое число')
    else:
        print('Сумма чисел:', summa(first_numb, second_numb))
    finally:
        print("Сработал Finally")
