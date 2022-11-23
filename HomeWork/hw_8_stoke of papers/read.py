import json

def read_data(file):
    with open(file) as r:
        read = json.load(r)
    return read

data = read_data('paper_stock.json')
print(data['paper'][1])

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
    return data_json

def find_data(data_json, find):
    for i in data_json['paper']:
            if find == i['brand'] or find == i['density'] or find == i ['size'] or find == i['surface']:
                print(i['id'], i['brand'], i['density'],i['size'],i['surface'], end=' ')
                id = i['id']
                for j in data_json['stock']:
                    if id == j['id']:
                        print(j['last arrival'], j['balance'])

