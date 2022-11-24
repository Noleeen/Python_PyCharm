import json

def add_data(data,file):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file, 'w', encoding= 'utf-8') as w:
        json.dump(data,w, indent=2)



a = {
    'paper':
    [
    {'brand':'sappy', 'density':'300g/m2', 'surface':'matt', 'size':'SRA3', 'id':'0001'},
    {'brand':'mondy', 'density':'200g/m2', 'surface':'matt', 'size':'A3', 'id':'0002'},
    {'brand':'mondy', 'density':'100g/m2', 'surface':'matt', 'size':'A3', 'id':'0003'},
    {'brand':'UPM', 'density':'300g/m2', 'surface':'gloss', 'size':'SRA3', 'id':'0004'}
    ],
    'stock':
    [
    {'last arrival': '15/05/22', 'balance': '520 sheets', 'id':'0001'},
    {'last arrival': '15/11/22', 'balance': '1000 sheets', 'id':'0002'},
    {'last arrival': '15/11/22', 'balance': '2000 sheets', 'id':'0003'},
    {'last arrival': '15/07/22', 'balance': '1520 sheets', 'id':'0004'}
    ]
    }
add_data(a,'paper_stock.json')
