def get_info():
    name = input('Enter name: ')
    sername = input('Enter sername: ')
    age = input('Enter age: ')
    lists = [name, sername, age]
    return lists


def w_file(info: list):
    text = ' '.join(info)
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


for i in range(10):
    w_file(get_info())
