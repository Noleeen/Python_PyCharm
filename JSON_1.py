import json

BD = [12345, True, 'яблоко', {"Міша": [898981546,54568465]}]


def load():
    # загрузить из json
    fname = 'BD.json' # открываем файл
    with open(fname, 'r', encoding = 'utf-8') as rd: # открываем файл на чтение
        BD_local = json.load(rd)
    print('БД загружена успешно')
    return BD_local

def save():
    # сохранить в json
    with open('BD.json', 'w', encoding= 'utf-8') as wr:
        wr.write(json.dumps(BD, ensure_ascii=False))
    print('БД загружена успешно')

# save()

BDnew = load()
print(BDnew)
