# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

print ('Введите данные для записи в файл \nДля окончания ввода введите пустую строку')
with open('text1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f"{line}\n")
