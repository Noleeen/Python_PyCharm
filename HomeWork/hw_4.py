# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def natural_num():
    check = True
    while check:
        try:
            num = int(input('enter natural number: '))
            if num <= 0:
                print('your enter is not natural number! repeat enter')
                continue
            check = False
        except ValueError as er:
            print('your enter is not natural number! repeat enter')
    return num


user_name = natural_num()
l = []
print(f'множетели числа {user_name}')
for n in range(2, user_name // 2 + 1):
    if user_name % n == 0:
        print(n, end=' ')
        l.append(n)
        for j in range(2, n // 2 + 1):
            if n % j == 0:
                l.pop()
                break

print(f'\n простые множители числа {user_name}:\n{l}')
