# 11. напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов: для 5 : 1,-3,9,-27,81
# a = int(input('enter number: '))
# b = 1
# for i in range(1, a):
#     print(b, end=', ')
#     b = b * -3
# else:
#     print(b)

# ещё один вариант
# a = int(input('enter number: '))
# lst = []
# for i in range(a):
#     lst.append((-3)**i)
# print(*lst, sep=", ")
# print(type(lst))

# 12. для натурального н создать строку из элементов
# последовательности 3н+1. для 6 (1:4, 2:7 .... 6:19)

# a = int(input('enter number '))
# some_str = ''
# li = []
# r = ':'
# for i in range(1, a+1):
#     li.append(f'{i}:' + str(3*i + 1))
#
# print(li)

# ещё один вариант
# a = int(input('enter number '))
# print('{', end="")
# for i in range(1, a):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{a}:{3 * a + 1}', end='}')


# 13. напишите программу в которой пользователь будет задавать две строки,
# а программа будет определять количество вхождений одной строки в другой

#
# n = input('enter string: ')
# n1 = input('enter string: ')
#
# if len(n) > len(n1):
#     count = 0
#     step = len(n1)
#     i = 0
#     while i < len(n):
#         if n[i:step + i] == n1:
#             count += 1
#         i += 1
#     print(count)
#
#
# elif len(n1) > len(n):
#     count = 0
#     step = len(n)
#     i = 0
#     while i < len(n1):
#         if n1[i:step + i] == n:
#             count += 1
#         i += 1
#     print(count)

#------------------------------------------------
# Программа по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти

# def diapason(num):
#     if num == 1:
#         print('x>0 y>0')
#     elif num == 2:
#         print('x<0 y>0')
#     elif num == 3:
#         print('x<0 y<0')
#     elif num == 4:
#         print('x>0 y<0')
#     else:
#         print('введите четверть от 1 до 4')
#
# try:
#     n = int(input('input number of quarter '))
#     diapason(n)
# except:
#     print('ввдено не чісло')

# расстояние между двумя точками

dim = int(input('enter the amount of coordinates '))
def create_list(dim):
    arr = [0]*dim
    for i in range(dim):
        try:
            arr[i] = float(input(f'input coordinate {i+1} '))
        except:
            print('нужно вводить вещественное число')
    return arr

def find_distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i]-b[i])**2
    distance = sum**0.5
    return distance

a = create_list(dim)
b = create_list(dim)
print(a)
print(b)
print(find_distance(a,b))

