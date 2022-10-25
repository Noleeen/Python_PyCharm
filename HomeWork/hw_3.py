# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

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

def mult(list):
    new_l = []
    for el in range(int(len(list) / 2)):
        new_l.append(list[el] * list[el * (-1) - 1])
    if len(list) % 2 != 0:
        new_l.append(list[int((len(list)) / 2)] ** 2)

    return new_l


try:
    l = [int(input(f"enter {i} number: ")) for i in range(int(input('enter length array: ')))]

    print(l)
    print(mult(l))

except ValueError as er:
    print(er)
