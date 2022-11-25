from logger import log

def p(data):
    print(data)


def main_menu():
    a = input('\n'
              'for read all data, enter "r" \n'
              'for find data, enter "f" \n'
              'for input new data, enter "new" \n'
              'for edit data, enter "e" \n'
              'for delete data, enter "d" \n'
              'for view log, enter "l" \n'              
              'for exit, enter "q" \n \n')
    return a

def user_find():
    u_find = input('input value for find: ')
    return u_find

def input_new_position(new_id):
    check = True
    while check:
        try:
            a = list(map(str, input('введите через "," поочерёдно следующие данные: \n '
                '"марка бумаги", "плотность", "поверхность", "формат","дата последней поставки", "остаток на складе(л)"\n'
                ' пример заполнения: "sappy,150g/m2,gloss,A3,01/05/2022,1400 sheets" \n').split(',')))
            paper = {'brand':a[0], 'density':a[1], 'surface':a[2], 'size':a[3], 'id':new_id}
            stock = {'last arrival': a[4], 'balance': a[5], 'id':new_id}
            check = 0
        except IndexError:
            print('Incorrect number of values entered! \n')

    log(f'add new data - id: {new_id}')
    return paper, stock

def edit_id():
    id = input('enter id position for edit: ')
    return id

def edit_copy_paste(old_dict):
    last_arrival = input(f'old value: {old_dict["last arrival"]}\nenter new value "last_arrival":\n ')
    balance = input(f'old value: {old_dict["balance"]}\nenter new value "balance":\n ')
    old_dict["last arrival"] = last_arrival
    old_dict["balance"] = balance
    return old_dict


def delete_id ():
    while True:
        del_id = input('enter id for delete: ')
        return del_id
