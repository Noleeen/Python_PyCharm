# постоянный цикл -поиск  факториала

# while True:
#     x = int(input('enter number '))
#     count = 0
#     temp = 1
#     while count < x:
#         count += 1
#         temp *= count
#     print(temp)

#______________________________________

# ввод данных
# x = ''
#
# while len(x) < 5:
#     y = input('enter data ')
#     if y == 'o': # если пользователь вводит "о" - пропускаем всё что ниже и возвращаемся в начало цикла
#         continue
#     if y == 'l': # если вводит 'l' - цикл прерывается и даже else не сработает
#         break
#     x = x + y
# else:
#     print(x)
# print('sd')

#------------------------------------------
# перебор списка (вывод списка на экран)

# for i in 'string text\'s':
#     print(i, end='')
# print('\nw hat else')


#-------------------------------------------
# ищем количество совпадений в двух строках

# x = 'йцукенгшщзхъэждлорпавыфюбьтимсчя.,'
# y = input('введите текст:\n')
# for i in x:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1
#     if count == 0:
#         continue
#     print(f'Букв {i} было {count}')


#--------------------------------------------
# range

for x in range(10,-11,-5):
    print(x)