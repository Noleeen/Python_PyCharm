# проверка ввода числа от пользователя

def check_input_int(text):
    check = False
    while not check:
        try:
            num = int(input(text))
            check = True
        except ValueError as error:
            print(f'please, enter integer number - {error}')
    return num

user_num = check_input_int('enter number: ')

# обратная итерация-----------------------------------------------------------------

# 1
# x = [1,2,3,4]
# for i in reversed(x):
#     print(i)
# x.reverse()
# print(x)

# 2
# x = [1,2,3,4]
# for i in range(len(x)-1, -1, -1):
#     print(i, x[i])
#
# print(x)

# 3
# x = [1,2,3,4]
# for i in x[::-1]:
#     print(i)
#
# print(x)


# 3
# x = [1,2,3,4]
# for i, el in reversed(list(enumerate(x))):
#     print(i, el)
#
# print(x)

#----------------------------------------------------------------------------------------------------