found = 0
words = input("Введите слово:")
simbol = input("Символ который ищем:")
for i in words:
    if i == simbol:
        found += 1
print(found)