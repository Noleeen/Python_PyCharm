from calc_View import user_input

def check_input(strr):

    check = 0
    while not check:
        strr = strr.replace('i', 'j')
        a = strr.replace('j', '')
        for el in a:
            if el.isalpha():
                print('input error!\n')
                strr = user_input()
            else:
                check = 1
    return strr


def complex_or_rational(data):
    data = data.replace('i', 'j')
    if 'j' in data:
        check = 'complex'
        return check

    else:
        check = 'rational'
        return check

