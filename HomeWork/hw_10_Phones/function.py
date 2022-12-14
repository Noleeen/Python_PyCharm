import json

def load(data, file):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file, 'w', encoding='utf-8') as w:
        json.dump(data, w, ensure_ascii=False, indent=2)


def read_data(file):
    with open(file, 'r', encoding='utf-8') as r:
        data_json = json.load(r)
    return data_json


def print_all(data_json):
    st = ''
    for k, v in data_json.items():
        st += f'{k}: {v}'
    st = str(st)
    st = st.replace('{', '\n')
    st = st.replace('}', '\n')
    st = st.replace('\'', ' ')
    return st


def generate_id(data_json):
    a = []
    for i in data_json:
        a.append(int(data_json[i]['id']))
        new_id = f'{(max(a) + 1):04}'
    return new_id


def add_new(data_json, file, new_data, new_id):
    new = {}

    new['phones'] = new_data[1]
    new['adress'] = new_data[2]
    new['birthday'] = new_data[3]
    new['e-mail'] = new_data[4]
    new['id'] = new_id
    data_json[new_data[0]] = new
    data_json = json.dumps(data_json)
    data_json = json.loads(str(data_json))
    with open(file, 'w', encoding='utf-8') as w:
        json.dump(data_json, w, ensure_ascii=False, indent=2)

def find(data_json, find_data):
    for k in data_json.keys():
        if k == find_data:
            data = f'<b>{k}</b>: \n ' \
                   f'phones: {data_json[k]["phones"]}\n ' \
                   f'adress: {data_json[k]["adress"]}\n ' \
                   f'birthday: {data_json[k]["birthday"]}\n ' \
                   f'e-mail: {data_json[k]["e-mail"]}\n' \
                   f'id: {data_json[k]["id"]}'
            return data
    else:
        return 'заданное значение не найдено'

def delete(data_json, find_data,file):
    check = 0
    for k in data_json.keys():
        if k == find_data:
            data_json.pop(k, 'deleted')
            with open(file, 'w', encoding='utf-8') as w:
                json.dump(data_json, w, ensure_ascii=False, indent=2)

            check = 1
            return 'контакт удалён'
    if check == 0:
        return 'заданное значение не найдено'


def edit(data_json, edit_data):
    for k in data_json.keys():
        if k == edit_data:
            data = f'{k} ' \
                   f'{data_json[k]["phones"]} ' \
                   f'{data_json[k]["adress"]} ' \
                   f'{data_json[k]["birthday"]} ' \
                   f'{data_json[k]["e-mail"]}'
            return data



