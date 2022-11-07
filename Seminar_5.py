# 36. Дан список чисел. Создайте список, в который попадают числа, описывающие
# максимальную возрастающую последовательность. Порядок элементов менять нельзя.
from builtins import print

# a = [1,5,3,4,8,2]
#
# def pos(s):
#     m = min(s)
#     # for x in s:
#     check = 1
#     while check:
#         if (m + 1) in s:
#             m += 1
#         else:
#             check = 0
#     res = [min(s),m]
#         # else:
#         #     s.remove(m)
#     return res
#
# print(pos(a))


# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв"

# a = ' сколько абв абвшек тут есть вбашкі счітаются'
# def rem(x):
#     c = x.split()
#     res = x.split()
#     print(res)
#     for i in c:
#         if 'абв' in i:
#             res.remove(i)
#     return res
# print(rem(a))

############################################
# второй способ
# a = ' сколько абв абвшек тут есть вбашкі счітаются'
# a = a.split()
# li = list(filter(lambda x: 'абв' not in x, a))
# print(f'{a} \n {li}')

##############################################
# удаляем все возможные сочетания запрашиваемых символов из строки

# a = ' сколько абв абвшек тут есть вбашкі счітаются'
# print(a.translate({ord(i):None for i in 'абв'}))

#######################################################
# 35. В файле находится N натуральных чисел записанных через пробел.
# Среди чисел не хватает одного, чтоб выполнялось условие А[i] - 1 = A[i-1]. Найдите это число

# with open('text.txt', 'r', encoding= 'utf-8') as t:
#     txt = list(map(int,t.readline().split(',')))
# print(txt)
# def find_num(l):
#     s = l.sort()
#     for ind in range(len(l)-1):
#         if l[ind] + 1 != l[ind + 1]:
#             print(l[ind] + 1)
# find_num(txt)
# print(txt)


########################################################
# 36 Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать в строку,  сворачивая соседние по числовому
# ряду числа в диапазоны.
# пример:
# [1,4,5,2,3,9,8,11,0] => '0-5,8-9,11'
# [1,4,3,2] => '1-4'
# [1,4] => '1,4'

a = [1, 4, 5, 2, 3, 9, 8, 11, 0]
a.sort()
print(a)
l_temp = []
l_res = ''

for el in a:
    if el + 1 in a:
        l_temp.append(el)
    else:
        if len(l_temp) >= 1:
            l_temp.append(el)
            l_res += f'{min(l_temp)}-{max(l_temp)}, '
            l_temp.clear()
        else:
            l_res += f'{el}, '
            l_temp.clear()
print(l_res.rstrip(', '))

