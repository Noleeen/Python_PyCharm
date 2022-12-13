from datetime import datetime as dt

def log(a,b):
    time = dt.now()
    with open('log.txt', 'a', encoding= 'utf-8') as l:
        l.write(f'{a} = {b} ; {time}\n')

def operator(l, znak):
    while znak in l:
        i = l.find(znak)
        count = 0
        while l[i+1].isdigit() or l[i+1] == '.':
            count += 1
            i += 1

        i = l.find(znak)
        if l[i-1] == ' ':
            break
        count2 = 0
        while l[i-1].isdigit() or l[i-1] == '.':
            count2 += 1
            i -= 1
        i = l.find(znak)

        if znak == '*':
            res1 =float(l[i-count2:i]) * float(l[i+1:i+count+1])
        elif znak == '/':
            res1 = float(l[i-count2:i]) / float(l[i+1:i+count+1])
        elif znak == '+':
            res1 = float(l[i-count2:i]) + float(l[i+1:i+count+1])
        elif znak == '-':
            res1 = float(l[i-count2:i]) - float(l[i+1:i+count+1])
        l = l[0:i-count2] + str(res1) +l[i+count+1:]
    return l

def complex(strr):
    strr = strr.replace('i', 'j')
    res = eval(strr)
    return res

