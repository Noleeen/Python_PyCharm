import json

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

print(phones['Силик'])
print(phones['Силик']['adress'])
print(len(phones['Паша']['phones']))

def load(data, file):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file, 'w', encoding='utf-8') as w:
        json.dump(data, w, ensure_ascii=False, indent=2)




load(phones, 'phones.json')