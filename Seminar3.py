
# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

# import time
# random_number = (int(str(time.time()).split('.')[1])) % 1000 # выводим трёхзначное случайное число
# print(random_number)



#-------------------------------------------------------------------------------------------------------
# 20. Задайте список. Напищите программу, которая определит, присутствует ли в заданном  списке строк некое число.

# n = int(input('enter length array: '))
# a = []
# for i in range(n):
#     a.append(input(f'enter {i+1} value: '))

#ТОЖЕ ТОЛЬКО ОДНОЙ СТРОКОЙ
# a = [int(input(f"enter {i+1} value: ")) for i in range(int(input('enter length array ')))]

# находим есть ли такой элемент в списке
# find = input('enter find value')
# if find in a:
#     print('yes')
# else:
#     print('no')
# print(a)

# находим есть ли наш элемент внутри элементов списка (т е есть ли в ['sdf5g', 'dsf', 'd'] значение '5' - да!)
# find = input('enter find value')
# for i in a:
#     if find in i:
#         print('yes')
#         break
# else:
#     print('no')




#-------------------------------------------------------------------------------------------------------
# 21.Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет

            # n = int(input('enter length array: '))
            # a = []
            # for i in range(n):
            #     a.append(input(f'enter {i+1} value: '))

        # s = [input(f"enter {i} value: ") for i in range(int(input('enter lengt array: ')))]
        # find_str = input('enter find value: ')
        # count = 0
        # for el in range(len(s)):
        #     if s[el] == find_str:
        #         count += 1
        #     if count == 2:
        #         print(el)
        #         break
        # else:
        #     print('-1')
        #
        #
        # print(s)

s = [ 'ff',6, 'fdg', 'ff', 55]
find_str = 'ff'
first = s.index(find_str)

second = s.index(find_str, first + 1)
print(second)