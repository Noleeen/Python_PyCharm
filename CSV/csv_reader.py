import csv

# просто считываем содержание файла
# with open('csv_1.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# считываем в виде словаря
with open('csv_1.csv',newline='') as r:
    re = csv.DictReader(r)
    for i in re:
        print(i['first'], i['second'])