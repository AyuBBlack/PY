name = input("Имя: ")


# Функция вывода текста
def print_name(x):
    print(x)


print_name(name)
print(id(print_name))
new_var = print_name
print(id(new_var))
