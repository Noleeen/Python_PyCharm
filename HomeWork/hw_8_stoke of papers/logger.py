from datetime import datetime as dt

def log(log_info):
    time = dt.now()
    with open('log.txt', 'a', encoding= 'utf-8') as l:
        l.write(f'{time} : {log_info}\n')