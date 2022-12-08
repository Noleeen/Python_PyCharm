import random
r = random.randint(0,1)
def ar(a):
    mas = ['-'] * a
    for c in range(a):
        mas[c] = ['-'] * a
    return mas

def print_a(a):
    for j in range(3):
        print("  ".join(a[j]))

def input_u():
    c = False
    while not c:
        try:
            row, column = map(int,input('enter row and column via space ').split())
            m = [row, column]
            c = 1
        except ValueError:
            print('error enter! repeat enter')
    return m

def ch3(ar):
    c = 0
    while not c:
        f = input_u()
        if 0 < f[0] < 4 and 0 < f[1] < 4:
            if ar[f[0]-1][f[1]-1] == '-':
                c = 1
            else:
                print('this cell is busy, move in free cell ')

        else:
            print('error enter! repeat enter')
    return f

def win(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[0][j] == l[1][j] == l[2][j] != '-' or l[i][0] == l[i][1] == l[i][2] != '-':
                win = 1
                return win
            else:
                win = 0
    if l[0][0] == l[1][1] == l[2][2] or l[2][0] == l[1][1] == l[0][2]:
        win = 1
    elif '-' not in l[1] + l[2] + l[0]:
        win = 2
    else:
        win = 0
    return win
def comp(l):
    a1 = (l[0][0], l[1][1], l[2][2])
    a2 = (l[2][0], l[1][1], l[0][2])
    if (a2.count('O') == 2 or a2.count('X') == 2) and '-' in a2:
        ind1 = a2.index('-')
        if '-' == l[2][0]:
            moveC = (2, ind1)
        if '-' == l[1][1]:
            moveC = (1, ind1)
        if '-' == l[0][2]:
            moveC = (0, ind1)
        return moveC

    elif (a1.count('O') == 2 or a1.count('X') == 2) and '-' in a1:
        ind2 = a1.index('-')
        if '-' == l[0][0]:
            moveC = (0, ind2)
        if '-' == l[1][1]:
            moveC = (1, ind2)
        if '-' == l[2][2]:
            moveC = (2, ind2)
        return moveC
    for i in range(len(l)):
        for j in range(len(l[i])):
            a = [l[0][j], l[1][j], l[2][j]]
            if (a.count('O') == 2 or a.count('X') == 2) and '-' in a:
                ind1 = a.index('-')
                moveC = (ind1, j)
                return moveC
            elif (l[i].count('O') == 2 or l[i].count('X') == 2) and '-' in l[i]:
                ind1 = l[i].index('-')
                moveC = (i,ind1)
                return moveC
    for i in range(len(l)):
        try:
            a = l[i].index('-')
            moveC = (i, a)
            return moveC
        except ValueError:
            a = 0


array = ar(3)
ch = True
move = 'X'
count = 0
while ch:
    print_a(array)
    print()
    if r:
        step = ch3(array)
        array[step[0] - 1][step[1] - 1] = move
    else:
        moveC = comp(array)
        array[moveC[0]][moveC[1]] = move

    r = not r
    count += 1
    if count > 4:
        winner = win(array)
        if winner == 1:
            print_a(array)
            if move == 'X':
                print('congratulation! winner X ')
            else:
                print('congratulation! winner O ')
            break
        elif winner == 2:
            print_a(array)
            print('game over. no winner')
            break
    if move == 'X':
        move = 'O'
    else:
        move = 'X'