############################################################
# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

############## ЗАПАКОВКА
# import sys
# with open('file2.txt',encoding='utf-8') as r:
#     f = r.read()
# def arc(f):
#     f += '*'
#     count = 0
#     res = ''
#     for i in range(1, len(f)):
#         if f[i] == f[i - 1] and count <= 7:
#             count += 1
#         else:
#             if count == 0:
#                 res += '1' + f[i - 1]
#             else:
#                 res += str(count + 1) + f[i - 1]
#                 count = 0
#     return res
# with open('file_end.txt', 'w', encoding='utf8') as w:
#     w.write(arc(f))
# print(f)
# print(arc(f))
# print(sys.getsizeof(f))
# print(sys.getsizeof(arc(f)))


############ РАСПАКОВКА
# with open('file_end.txt', encoding='utf-8') as r:
#     f = r.read()
# def unzip(f):
#     res = ''
#     for ind in range(0,len(f),2):
#         res += f[ind+1] * int(f[ind])
#     return res
#
# with open('file2.txt', 'a', encoding='utf8') as w:
#     w.write('\n' + unzip(f))
#
# print(f)
# print(unzip(f))


#############################################################
# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
# a = input('enter string: ')
# a = a.split()
# res = list(filter(lambda x: 'абв' not in x, a))
# print(a)
# print(res)

##############################################################
# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
#
# a = '5*x^3+2*x^2+6'.split('+')
# b = '7*x^2+6*x+3'.split('+')
#
# last_coef = 0
# def in_sp(d):
#     global last_coef
#     l_a = []
#     for el in d:
#         if '*' in el:
#             l_a.append(el.split('*'))
#         else:
#             last_coef += int(el)
#     return l_a
# def dic(d):
#     sl = {}
#     for el in d:
#         sl[el[1]] = int(el[0])
#     return sl
#
# a = dic(in_sp(a))
# b = dic(in_sp(b))
#
# for x in a.keys():
#     for y in b.keys():
#         if x == y:
#             b[y] += a[x]
# c = a | b
#
# for d,f in c.items():
#     print(f'{f}*{d} + ', end='')
# print(f'{last_coef}')


##############################################################
# задача 5 необязательная: Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1,  5]


# a = [1, 5, 2, 3, 4, 1, 7, 8 , 9, 10, 11, 12, 15 , 1 ]
# print(a)
# a.sort()
# l_temp = []
# l_max = []
# l_res = []
#
# for el in a:
#     if el + 1 in a:
#         if el not in l_temp:
#             l_temp.append(el)
#     else:
#         if len(l_temp) + 1 > len(l_max):
#             l_temp.append(el)
#             l_res = [min(l_temp), max(l_temp)]
#             l_max = l_temp.copy()
#             l_temp.clear()
#
# print(l_res)
