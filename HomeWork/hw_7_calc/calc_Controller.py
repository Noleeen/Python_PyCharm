from calc_Rational_numbers import rational
from calc_Complex_numbers import complex
from calc_Input_validation import*
from calc_View import*
from calc_Logger import log

def e():
    a = check_input(user_input())
    return a

expression = e()

def solution(exp):
    check_expression = complex_or_rational(exp)
    if check_expression == 'complex':
        res = complex(exp)
    elif check_expression == 'rational':
        res = rational(exp)

    return res

res = solution(expression)

def view_end():
    log(expression, res)
    view_result(res)


