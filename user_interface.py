from controller import button_click as bc
from print_phonebook import print_phonebook as pp

print()
print('Это телефонный справочник, импортирующий записи в .csv, .xml и .html форматы. Для начала работы нажмите Enter')
input()

user_input = int(input('Желаете внести запись в телефоную книгу? Нажмите 1 \nЖелаете посмотреть существующие записи? Нажмите 2. \n >>> '))

if user_input == 1:
    bc()
elif user_input == 2:
    pp()


print()


