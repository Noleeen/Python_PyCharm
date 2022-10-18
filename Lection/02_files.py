# while True:
#     import Seminar_2
#     print(Seminar_2.fun(int(input('напішыце ўзрост: '))))

#-------------------------------------------------------------------
# числа фибоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range(3,10):
#     list.append(fib(e))
# print(list)
#---------------------------------------------------------------------




exit()

path = 'file.txt'
read = open(path, 'r')
for d in read:
    print(d, end='')
read.close()

with open('file.txt', 'w') as x:
    x.write('\nnew text')

# exit()
text = ['hello2', 'my dear33', 'friend']
add_data = open('file.txt', 'a')
add_data.writelines(f'\n{text}')
add_data.write('\n new string\n\n')
add_data.write('\n cat')
add_data.close()
