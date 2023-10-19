n = int(input('Введите длину списка:'))
user_list =[]

i=0
while i < n:
    string = "Введите номер элемента #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)