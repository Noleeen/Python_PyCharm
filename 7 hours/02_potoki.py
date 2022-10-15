# запуск сайта введённого пользователем

import os

while True: # постоянный цикл
    sayt = input('input website \n')

    if sayt == "end": # выход из цикла
        break

    if 'https://' in sayt:
        os.system('start ' + sayt)
        print('if')
    elif 'www.' in sayt:
        sayt = "https://" + sayt
        os.system('start ' + sayt)
        print('elif')
    else:
        sayt = "https://www." + sayt
        os.system('start ' + sayt)
        print('else')

# запуск файла с компьютера
# import os
# import time
#
# os.system('start https://www.youtube.com/') # просто так открываем сайт
# time.sleep(7) # код останавлівается на 7 секунд
# os.startfile('C://Windows/system32/cmd.exe')