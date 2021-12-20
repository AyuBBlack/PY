try:
    with open('../data/text.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл не найден')
