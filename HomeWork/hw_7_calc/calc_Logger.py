from datetime import datetime as dt

def log(a,b):
    time = dt.now()
    with open('log.txt', 'a', encoding= 'utf-8') as l:
        l.write(f'{a} = {b} ; {time}\n')

