# # словарі
#
# # регистр
#
# a = 'sdFsd FSA'
#
# print(a.capitalize()) # Sdfsd fsa
# print(str.capitalize(a)) # Sdfsd fsa
# print('sdFsd FSA'.capitalize()) # Sdfsd fsa
#
# print(a.casefold()) # sdfsd fsa
# print(str.casefold(a)) # sdfsd fsa
# # Функция str.casefold() возвращает свернутую копию строки. Понятие «свернутая копия» строки означает, что в такой копии удалены все отличия регистра символов в строке.
# # Особенность «свернутой» копии строки состоит в том, что функция lower() не может быть применена к некоторым символам, а функция casefold() может. Примером такого символа есть немецкий символ ‘ß’, который в функции casefold() заменяется на символы ss в отличие от функции lower().
#
# print(a.lower()) # sdfsd fsa
# print('FGsfdf F dfdD'.lower()) # fgsfdf f dfdd
#
# print(a.swapcase())# SDfSD fsa
#
# print(a.title()) # Sdfsd Fsa
# # Отдельный случай с символом апострофа '\''
# # s1 = "I'm happy!"
# # s2 = s1.swapcase() # s2 = 'i'M HAPPY!'
#
# print(a.upper()) # SDFSD FSA

####################################################################
# словарь

def num_translate(key, dict):
    print(dict[key])


d = {'one': 'один', 'two': 'два', 'four': 'три'}
user_text = input('enter word: ').lower()
num_translate(user_text, d)
