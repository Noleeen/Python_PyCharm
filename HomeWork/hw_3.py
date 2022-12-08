# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def sum_odd(list):
#     sum = 0
#     for i in range(1, len(list), 2):
#         sum += list[i]
#     return sum
#
#
# try:
#     l = [int(input(f'enter {i} value: ')) for i in range(int(input('enter length array: ')))]
#
#     print(sum_odd(l))
#
# except:
#     print('enter integer number')

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def mult(list):
#     new_l = []
#     for el in range(int(len(list) / 2)):
#         new_l.append(list[el] * list[el * (-1) - 1])
#     if len(list) % 2 != 0:
#         new_l.append(list[int((len(list)) / 2)] ** 2)
#
#     return new_l
#
#
# try:
#     l = [int(input(f"enter {i} number: ")) for i in range(int(input('enter length array: ')))]
#
#     print(l)
#     print(mult(l))
#
# except ValueError as er:
#     print(er)

# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# def diff(l):
#     max = 0
#     min = round(l[0] % 1, 7)
#     for i in range(len(l)):
#         if l[i] < 0:
#             l[i] *= -1
#         if type(l[i]) == type(0.1):
#             if l[i] % 1 > max:
#                 max = round(l[i] % 1, 7)
#             if l[i] % 1 < min:
#                 min = round(l[i] % 1, 7)
#     differ = max - min
#     return differ
#
#
# s_l = [1.1, 1.2, 3.1, 5, -10.01]
# print(s_l)
# print(diff(s_l))


#----------------------------------------------------------------------------------
# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.

            # c = int(input())
            # print(bin(c)[2:])

while True:
    a = (int(input()))
    b = []
    while a != 0:
        b.append(a % 2)
        a //= 2

    print(''.join(map(str, b[::-1])))


