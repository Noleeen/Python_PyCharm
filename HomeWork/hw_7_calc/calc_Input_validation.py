def input_valid(strr):
    strr = strr.replace(' ', '')
    strr = strr.replace('i', 'j')
    a = strr.replace('j', '')
    for el in a:
        if el.isalpha():
            return print('input error')
    if 'j' in strr:
        str_complex = strr
        return str_complex

    else:
        str_rational = strr
        return str_rational