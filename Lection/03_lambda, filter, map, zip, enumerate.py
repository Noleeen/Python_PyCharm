# берём из файла строку цифр разделённых пробелом, считываем их, циклом (используя пробел, как разделитель) преобразовываем
# каждое число в int и аписываем в новый список, потом исп функцию и создаём кортеж из чётных чисел и их куба
# r = open('file.txt', 'r')
# data = r.read() + ' '
# r.close()
#
# print(data)
# print(type(data))
#
# numbers =[]
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# print(numbers)
#
# pow = lambda i: i**3
# l = [(i,pow(i)) for i in numbers if i % 2 == 0]
# print(l)

#############################################################
# то же самое:

# def select(f, col):
#     return[f(x) for x in col]
# def where(f, col):
#     return[x for x in col if f(x)]
#
# data = '1 2 3 4 5 8 6 77 55'
# d = data.split()
#
# res = select(int, d)
# res = where(lambda i: not i%2, res)
# res = select(lambda x: (x, x**3),res)
#
# print(res)

###########################################
# то же самое только с MAP и FILTER

li = '1 2 3 5 4 6'
res_to_int = list(map(int,li.split()))
# или, например  другую ф-ию: res = list(map(lambda x: x+10, li))
res_to_if = list(filter(lambda x: x%2 == 0, res_to_int))
res_to_cube = list(map(lambda x:(x,x**3),res_to_if))

print(res_to_int)
print(res_to_if)
print(res_to_cube)

