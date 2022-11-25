import view
import operations as op

check = False
while not check:
    run = view.main_menu()
    data_json = op.read_data('paper_stock.json')
    if run == 'r':
        op.print_all_list(data_json)
    elif run == 'f':
        find_value = view.user_find()
        op.find_data(data_json, find_value)
    elif run == 'new':
        new_id = op.generate_id(data_json)
        new_tuple = view.input_new_position(new_id)
        op.add_new_data(data_json, 'paper_stock.json', new_tuple)
    elif run == 'e':
        edit_id = view.edit_id()
        op.edit_stock(data_json, edit_id)







# удаление строки по id
del_id = view.delete_id()
if del_id == 0:
    view.main_menu()
else:
    operations.delete(data,del_id)






