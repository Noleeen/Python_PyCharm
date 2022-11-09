# задача 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

from random import randint as r


sweets = 221
rand = r(0, 1)


def check_int():
    c = False
    while not c:
        try:
            num = int(input())
            c = True
        except ValueError:
            print(f'input error! enter a number in the range from 1 to 28')
    return num


def check_28():
    c = False
    while not c:
        f = check_int()
        if 1 <= f <= 28:
            c = True
        else:
            print(f'input error! enter a number in the range from 1 to 28')
    return f

######## игрок с игроком
# while sweets > 0:
#     print(f'now {sweets} sweets')
#     if rand == 1:
#         print('player 2: ')
#     else:
#         print('player 1: ')
#     move = check_28()
#     sweets -= move
#     rand = not rand
#
# if rand == 0:
#     print('Congratulation! player 2 win!')
# else:
#     print('Congratulation! player 1 win!')

######## игрок с умным компом
def bot(x):
    a = x % 28
    if (x//28) % 2 == 0:
        if a == 0:
            y = 27
        elif a == 1:
            y = 28
        else:
            y = a - 1
    else:
        y = a - 1
        if y < 1:
            y = 28
    return y

while sweets > 0:
    print(f'now {sweets} sweets')
    if rand == 1:
        move = bot(sweets)
        print(f'comp:\n {move} ')
    else:
        print('player: ')
        move = check_28()
    sweets -= move
    rand = not rand

if rand == 0:
    print('Congratulation! computer win!')
else:
    print('Congratulation! player win!')