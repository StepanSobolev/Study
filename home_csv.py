import json
import csv

with open('data.json', 'r', encoding='utf-8') as file_data:
    data = json.load(file_data)

with open('dictwriter.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['', 'Person1', 'Person2', 'Person3'])
    id = []
    id.insert(0, 'id')
    name = []
    name.insert(0, 'name')
    age = []
    age.insert(0, 'age')

    for i in data.keys():
        id.append(i)

    for nam, ag in data.values():
        name.append(nam)
        age.append(ag)

    writer.writerow(id)
    writer.writerow(name)
    writer.writerow(age)
    writer.writerow(['phone', '5555555', '6666666', '777777777', '88888888', '99999999', '333333333', '22222222'])






