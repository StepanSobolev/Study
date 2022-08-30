name = input('Введите имя:')
profession = input('Введите професию: ')
education = input('Введите образование: ')
adress = input('Введите адрес: ')

with open('library.txt', 'w', encoding='UTF-8') as data:
    data.write(name + '\n')
    data.write(profession + '\n')

with open('library.txt', 'a', encoding='UTF-8') as data:
    data.write(education + '\n')
    data.write(adress + '\n')