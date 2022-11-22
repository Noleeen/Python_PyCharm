import csv

# просто записать в файл итерируемый объект (строку разобъёт посимвольно)
# with open('csv_1.csv', 'w', newline='') as f:
#     wr = csv.writer(f)
#     wr.writerow(['sdf','sdfsdgsgs fg fg ',1])


#  записать в файл в виде словаря
with open('csv_1.csv', 'w') as w:
    head = ['first', 'second']
    writer = csv.DictWriter(w, fieldnames=head, delimiter = ';')

    writer.writeheader()
    writer.writerow({'first': 'Baked', 'second': 'Deans'})
    writer.writerow({'first': 'Lars', 'second': 'Loril'})
    writer.writerow({'first': 'Ivan', 'second': 'Grovel'})