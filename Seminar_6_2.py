# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
#
# 2+2 => 4;
#
# 1+2*3 => 7;
#
# 1-2*3 => -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#
# *Пример:*
#
# 1+2*3 => 7;
#
# (1+2)*3 => 9;

# l = input('enter expression: ')
l = '5 + 30 / 15 * 2 *2-25'
l = l.replace(' ','')
l = ' ' + l + ' '
print(l)
def operator(l,znak):
    while znak in l:
        i = l.find(znak)
        count = 0
        while l[i+1].isdigit():
            count += 1
            i += 1
        i = l.find(znak)
        count2 = 0
        while l[i-1].isdigit():
            count2 += 1
            i -= 1
        i = l.find(znak)

        if znak == '*':
            res1 = int(l[i-count2:i]) * int(l[i+1:i+count+1])
        elif znak == '/':
            res1 = int(l[i-count2:i]) / int(l[i+1:i+count+1])
        elif znak == '+':
            res1 = int(l[i-count2:i]) + int(l[i+1:i+count+1])
        elif znak == '-':
            res1 = int(l[i-count2:i]) - int(l[i+1:i+count+1])
        l = l[0:i-count2] + str(res1) +l[i+count+1:]
    return l


l = operator(l,'*')
l = operator(l,'/')
l = operator(l,'+')
l = operator(l,'-')


print(l)


