def p(data):
    print(data)


def main_menu():
    a = input('for read all data, enter "1" \n'
              'for find data, enter "2" \n'
              'for input new data, enter "3" \n'
              'for edit data, enter "4" \n'
              'for exit, enter "q" \n')
    return a


def input_new_position(new_id):
    a = list(map(str, input('введите через "," поочерёдно следующие данные: \n '
            '"марка бумаги", "плотность(г/м2)", "поверхность", "формат","дата последней поставки", "остаток на складе(л)"\n'
            'пример заполнения: "sappy, 150, gloss, A3, 01/05/2022, 1400" \n').split(',')))
    paper = {'brand':a[0], 'density':a[1], 'surface':a[2], 'size':a[3], 'id':new_id}
    stock = {'last arrival': a[4], 'balance': a[5], 'id':new_id}
    return paper, stock

def edit_id():
    id = input('enter id position for edit')
    return id

def edit_copy_paste(old_dict):
    new_dict = input(f'copy, paste and edit this string:\n {old_dict}\n')
    return new_dict

f = edit_copy_paste('sdfsf')
print(f)