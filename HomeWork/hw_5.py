# задача 5 необязательная: Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1,  5]

a = [1, 5, 2, 3, 4, 1, 7, 8 , 9, 10, 11, 12, 15 , 1 ]
print(a)
a.sort()
l_temp = []
l_max = []
l_res = []

for el in a:
    if el + 1 in a:
        if el not in l_temp:
            l_temp.append(el)
    else:
        if len(l_temp) + 1 > len(l_max):
            l_temp.append(el)
            l_res = [min(l_temp), max(l_temp)]
            l_max = l_temp.copy()
            l_temp.clear()

print(l_res)
