import json
import pprint

phones = {'Силик':
              {'phones': ['123','54567'],
               'adress' : 'Минск',
               'birthday' : '01.05.1987',
               'e-mail' : 'sdf@tut.by',
               'id' : '0001'},
          'Паша':{'phones': ['126','554667'],
               'adress' : 'Лондон',
               'birthday' : '13.05.1986',
               'e-mail' : 'sd@tut.by',
                'id' : '0001'}}

# print(phones['Силик'])
# print(phones['Силик']['adress'])
# print(len(phones['Паша']['phones']))






def read_data(file):
    with open(file, 'r', encoding='utf-8') as r:
        read = json.load(r)
    return read


def generate_id(data_json):
    a = []
    for i in data_json:
        a.append(int(data_json[i]['id']))
        new_id = f'{(max(a) + 1):04}'
    return new_id






print(generate_id(read_data('phones.json')))
# print(pars(print_all(read_data('phones.json'))))

