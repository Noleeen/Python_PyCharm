# кортеж в список

# t = (94,93,32)
# d = list(t)
# print(t)
# print(d)
#
# bd = {'el1' : t}
# print(bd)
#
# bd['el1'] = list(bd['el1'])
# print(bd)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# num = int(input('enter number: '))

# fib = [0,1]
#
# n = 10
# for i in range(2,n+1):
#     fib.append(fib[i-1] + fib[i-2])
#
# fib2 = []
# for i in range(2,len(fib)):
#     if i % 2 ==0:
#         fib2.append(fib[i] * -1)
#     else:
#         fib2.append(fib[i])
# fin = fib2[::-1] + fib
#
# print(fib)
# print(fib2)
# print(fin)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) с помощью математических формул нахождения корней квадратного уравнения

# # через sympy
# import sympy as sm
# a, b, c = map(int, input('enter a,b,c via space: ').split())
# x = sm.Symbol('x')
# print(sm.solveset(a*x**2 + b*x +c))

#АЛГОРІТМОМ
# a = 0
# b = 6
# c = 5
# d = discriminant = b ** 2 - 4 * a * c
#
# if a == 0:
#     print(f'x = {-c / b}')
# else:
#     if d < 0:
#         print('no root of the equation')
#     else:
#         x1 = (-b + d ** 0.5) / 2 * a
#         x2 = (-b - d ** 0.5) / 2 * a
#         print('x1 = ', x1, ', x2 = ', x2)

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#
# # ___________________________________________
# # решение через НОК
# a, b = map(int, input('enter number via space: ').split())
# for i in range (min(a,b), a * b + 1, min(a,b)):
#     if i % a == 0 and i % b == 0:
#         print(f'nok = {i}')
#         break
# # ____________________________________________

# второе решеніе через НОД

# def chek_number(t):
#     check = False
#     while not check:
#         try:
#             num = int(input(t))
#             check = True
#         except ValueError as er:
#             print(f'enter float number - {er}')
#     return num
# a = chek_number('enter number: ')
# b = chek_number('enter number: ')
#
# for i in range(min(a,b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         nod = i
#         break
#
# nok = a * b / nod
# print(nok)

#------------------------------------------------------------------
# задайте строку из набора чисел. напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя исп пробел.

# n = list(map(int, input('enter numbers: ').split(' ')))
# minn = min(n)
# maxx = max(n)
#
# # n = list(string)
# print(f'{n}\nmin = {min(n)}\nmax = {max(n)}')





