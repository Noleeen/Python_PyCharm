# 36. Дан список чисел. Создайте список, в который попадают числа, описывающие
# максимальную возрастающую последовательность. Порядок элементов менять нельзя.

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
a = ' сколько абв абвшек тут есть вбашкі счітаются'

print(a.translate({ord(i):None for i in 'абв'}))