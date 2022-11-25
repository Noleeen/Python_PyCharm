import json
import view
from logger import log

def read_data(file):
    with open(file) as r:
        read = json.load(r)
    return read

def read_log(file):
    with open(file) as r:
        print(r.read())


def print_all_list(data_json):
    for i in data_json['paper']:
        print(i['id'],'     ', i['brand'],'     ', i['density'],'     ', i['size'],'     ', i['surface'],'     ', end=' ')
        id = i['id']
        for j in data_json['stock']:
            if id == j['id']:
                print(j['last arrival'],'     ', j['balance'])


def generate_id(data_json):
    a = []
    for i in data_json['paper']:
        a.append(int(i['id']))
        new_id = f'{(max(a) + 1):04}'
    return new_id

def add_new_data(data_json, file, new_tuple):
    data_json['paper'].append(new_tuple[0])
    data_json['stock'].append(new_tuple[1])
    data_json = json.dumps(data_json)
    data_json = json.loads(str(data_json))
    with open(file, 'w', encoding= 'utf-8') as w:
        json.dump(data_json,w, indent=2)
    print('addition made')

def find_data(data_json, find):
    check = 0
    for i in data_json['paper']:
        if find == i['brand'] or find == i['density'] or find == i ['size'] or find == i['surface']:
            print(i['id'], i['brand'], i['density'],i['size'],i['surface'], end=' ')
            id = i['id']
            check = 1
            for j in data_json['stock']:
                if id == j['id']:
                    print(j['last arrival'], j['balance'])
    if check == 0:
        print(f'value {find} not found')

def edit_stock(data_json, edit_id):
    l = data_json['stock']
    c=0
    for j in range(len(l)):
        if edit_id == l[j]['id']:
            c=1
            a = l[j].copy()
            new_dict = view.edit_copy_paste(l[j])
            log(f'edit data - id: {edit_id}\n old_data: {a}\n new_data: {new_dict}')
            l[j] = new_dict
            data_json['stock'] = l
            print('edits applied:')
            return data_json
    if c == 0:
        print(f'id {edit_id} not found')
        return data_json

def write_edit_data(data_json, file):
    with open(file, 'w', encoding= 'utf-8') as w:
        json.dump(data_json,w, indent=2)


def delete(data_json, delete_id):
    m = data_json['paper']
    l = data_json['stock']
    m_del_ind = 0
    l_del_ind = 0
    for j in range(len(m)):
        if delete_id == m[j]['id']:
            m_del_ind = j
            break
        else:
            m_del_ind = "not found"

    if m_del_ind == "not found":
        print('entered index not found')
        return False
    else:
        check = input(f'would you like delete data with {delete_id} id?\n'
                      f'{m[m_del_ind]}, {l[m_del_ind]} \nenter "yes" or "no": ')
        if check == "yes":
            del m[m_del_ind]
            data_json['paper'] = m
            del l[m_del_ind]
            data_json['stock'] = l
            log(f'delete data - id: {delete_id}')
            print(f'data with id {delete_id} deleted')
            return data_json
        elif check == "no":
                return False
        else:
            print('you entered incorrect command')
            return False
