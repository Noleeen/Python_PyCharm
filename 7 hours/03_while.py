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
x = ''

while len(x) < 5:
    y = input('enter data ')
    if y == 'o': # если пользователь вводит "о" - пропускаем всё что ниже и возвращаемся в начало цикла
        continue
    if y == 'l': # если вводит 'l' - цикл прерывается и даже else не сработает
        break
    x = x + y
else:
    print(x)
print('sd')




