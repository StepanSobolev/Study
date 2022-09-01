import json

def new_wook():
    data = {}
    name = ('Jon', 'Лев', 'Иван', 'Даниил', 'Василиса', 'Екатерина', 'Вера')
    age = (25, 26, 35, 62, 39, 56, 15)
    for i in range(0, 7):
        data[100000 + i] = (name[i], age[i])
    return data

with open('data.json', 'w') as file_data:
    json.dump(new_wook(), file_data)