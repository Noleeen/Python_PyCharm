def rational(l):
    l = l.replace(' ', '')
    l = ' ' + l + ' '

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


    while '(' in l:
        ind_1 = l.find('(')
        ind_2 = l.find(')')
        l_temp = ' ' + l[ind_1+1 : ind_2] + ' '
        l_temp = operator(operator(operator(operator(l_temp,'*'),'/'),'+'), '-')
        l_temp = l_temp.replace(' ','')
        l = l[:ind_1] + l_temp + l[ind_2+1:]

    result = operator(operator(operator(operator(l,'*'),'/'),'+'), '-')
    return result

