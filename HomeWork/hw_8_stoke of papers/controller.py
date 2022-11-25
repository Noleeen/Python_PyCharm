import view
import operations as op

def run_paper_stock():
    check = False
    while not check:
        run = view.main_menu()
        data_json = op.read_data('paper_stock.json')
        if run == 'r': # выводим в консоль таблицы из файла
            op.print_all_list(data_json)
        elif run == 'f': # запускаем поиск по заданному значению и выводим результат в консоль
            find_value = view.user_find()
            op.find_data(data_json, find_value)
        elif run == 'new': # добавляем новую строку в таблицы: генерируем новый id , пользователь вносит новые данные, записываем их в сенерированный id
            new_id = op.generate_id(data_json)
            new_tuple = view.input_new_position(new_id)
            op.add_new_data(data_json, 'paper_stock.json', new_tuple)
        elif run == 'e': # редактирование: запрашиваем id у пользователя, выводим старые данные по id в консоль, пользователь их копирует, вставляет и исправляет. после этого перезаписываем файл.
            edit_id = view.edit_id()
            data = op.edit_stock(data_json, edit_id)
            op.write_edit_data(data, 'paper_stock.json')
        elif run == 'd': # запрашиваем у пользователя id для удаления, показываем ему строку, которую он собирается удалить и уточняем, точно ли он собирается её удалить, затем удаляем все данные с этим id, перезаписываем файл
            del_id = view.delete_id()
            data = op.delete(data_json,del_id)
            if data == False:
                continue
            op.write_edit_data(data, 'paper_stock.json')
        elif run == 'l':
            log = op.read_log('log.txt')
        elif run == 'q': # quit - выходим из цикла
            check = not check
        else:
            print("command entered incorrectly, repeat enter, please.\n")















