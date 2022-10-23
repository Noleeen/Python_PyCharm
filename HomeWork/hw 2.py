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

# решеніе с пом строкі
# n = input()
# s = 0
# for i in n:
#     if i.isdigit():
#         s += int(i)
# print(s)

# ----------------------------------------------------------------------
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

# задайте список из N элементов, заполненных числами из промежутка [-N:N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в дной строке одно число

import random

n = int(input())
l = []
for _ in range(n):
    l.append(random.randint(-n, n))
print(l)
with open('file2.txt', 'w', encoding='utf-8') as f:
    for _ in range(random.randint(1, n)):
        f.write(str(random.randint(0, n - 1)) + '\n')
fact = 1
with open('file2.txt', 'r', encoding='utf-8') as rf:
    n_rf = rf.read().splitlines()
    for i in n_rf:
        fact *= l[int(i)]
print(fact)

exit()
# ------------------------------------------------------
# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

dim = int(input('enter the amount of coordinates '))


def create_list(dim):
    # arr = [0]*dim
    arr = []
    for i in range(dim):
        try:
            arr.append(float(input(f'input coordinate {i + 1} ')))
            # arr[i] = float(input(f'input coordinate {i+1} '))
        except:
            print('нужно вводить вещественное число')
    return arr


def find_distance(a, b):
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i] - b[i]) ** 2
    distance = sum ** 0.5
    return distance


a = create_list(dim)
b = create_list(dim)

print(find_distance(a, b))
