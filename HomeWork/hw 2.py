# Задача 1. Напишите программу, которая принимает на вход вещественное или целое
# число и показывает сумму его цифр. Через строку нельзя решать.
# while True:
#     num = float(input('enter number '))
#     temp = 0
#     if num < 0:
#         num *= -1
#     while num%1 != 0:
#         num *= 10
#     while num != 0:
#         temp = temp + num % 10
#         num = num // 10
#     print(f'sum digits = {temp}')

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

# num = int(input('enter number '))
# i = 1
# temp = 1
# print('[ ', end='')
# while i < num:
#     temp *= i
#     i += 1
#     print(temp, end=', ')
# print(f'{temp * num} ]')

# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# str_1 = input('enter string1: ')
# str_2 = input('enter string2: ')
#
# if len(str_1) >= len(str_2):
#     i = 0
#     count = 0
#     while i < len(str_1):
#         if str_1[i: len(str_2)+i] == str_2:
#             count += 1
#         i += 1
#     print(count)
# elif len(str_1) < len(str_2):
#     i = 0
#     count = 0
#     while i < len(str_2):
#         if str_2[i: len(str_1)+i] == str_1:
#             count += 1
#         i += 1
#     print(count)



