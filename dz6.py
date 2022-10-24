# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.
# модуль для расчетов операций
import cmath

# def Calc_block(data):
#     left_value, oper, right_value = data
#     if oper == '+':
#         return sum(left_value, right_value)
#     if oper == '-':
#         return sub(left_value, right_value)
#     if oper == '*':
#         return mult(left_value, right_value)
#     if (oper =='/') and (right_value != 0):
#         return div(left_value, right_value)
#     else:
#         return 'Ошибка деления на 0!'
#
# def sum(left_value, right_value):
#     return left_value + right_value
#
# def sub(left_value, right_value):
#     return left_value - right_value
#
# def mult(left_value, right_value):
#     return left_value * right_value
#
# def div(left_value, right_value):
#     return left_value / right_value
#
# def mult(left_value, right_value):
#     return left_value * right_value
#
# def div(left_value, right_value):
#     return left_value / right_value
#
#
#
# def data_formatting(data):
#     data_type, left_value, oper, right_value = data
#
#     if data_type == '1':
#
#         left_value = complex(left_value)
#
#         right_value = complex(right_value)
#
#     elif data_type == '2':
#
#         a = left_value
#         left_value = Fraction(int(a[0: a.index(
#             '/')]), int(a[a.index('/')+1:len(a)]))
#
#         g = right_value
#         right_value = Fraction(int(g[0: g.index(
#             '/')]), int(g[g.index('/')+1:len(g)]))
#
#     return (left_value, oper, right_value)

# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# def readfile(filename):
#     # чтение файла при запуске
#     return open(filename).read().split('\n')
#
#
# def scan(data):
#     # Просмотр всех записей справочника:
#     for i in data:
#         print(i)
#
#
# def search(data):
#     # Поиск по справочнику.
#     flag = 1
#     name = input('имя > ')
#     for line in data:
#         if name in line:
#             flag = 0
#             print(line)
#     if flag: print('no name given')
#
#
# data = readfile('data.txt')  # При запуске программы (скрипта), она должна считывать содержимое
# dict_command = {'1': scan, '2': search}  # словарь команд, в значениях функции их исполняющие
#
# print('''Команды для работы со справочником:
#     Просмотр всех записей справочника:  - 1
#     Поиск по справочнику -2
#     Добавление новой записи - 3
#      Удаление записи из справочника по Имени и Фамилии - 4
#      Изменение любого поля в определенной записи справочника - 5
#      Вывод возраста человека (записи) по Имени и Фамилии - 6 ''')
#
# while True:
#     command = input('Команда: > ')
#     if command in dict_command:
#         dict_command[command](data)
#     else:
#         print(' command error!')
