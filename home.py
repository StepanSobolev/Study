import time


def listner():
    print('Обработка результата')
    for i in range(20):
        print('.', end='')
        time.sleep(.3)
    print()

while True:
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    if not age.isdigit() or int(age) <= 0:
        listner()
        print('Ошибка, повторите ввод, возраст должен состоять только из цыфр')
        # print('Желаете выйти? (Д/Y): ')
        # time.sleep(1)
        # print('Желаете продолжить нажмите Enter: ')
        # cont = input()
        # if cont.lower() == 'д' or cont.lower() == 'y':
        #     break
        # else:
        #     continue
    elif 0 < int(age) < 10:
        listner()
        print(f'Привет, шкет {name}')
        print('Желаете выйти? (Д/Y): ')
        time.sleep(1)
        print('Желаете продолжить нажмите Enter: ')
        cont = input()
        if cont.lower() == 'д' or cont.lower() == 'y':
            break
        else:
            continue
    elif 10 <= int(age) <= 18:
        listner()
        print(f'Как жизнь {name}')
        print('Желаете выйти? (Д/Y): ')
        time.sleep(1)
        print('Желаете продолжить нажмите Enter: ')
        cont = input()
        if cont.lower() == 'д' or cont.lower() == 'y':
            break
        else:
            continue
    elif 18 < int(age) < 100:
        listner()
        print(f'Что желаете {name}')
        print('Желаете выйти? (Д/Y): ')
        time.sleep(1)
        print('Желаете продолжить нажмите Enter: ')
        cont = input()
        if cont.lower() == 'д' or cont.lower() == 'y':
            break
        else:
            continue
    else:
        listner()
        print(f'{name}, вы лжете - в наше время столько не живут...')
        time.sleep(1)
        print('Желаете выйти? (Д/Y): ')
        time.sleep(1)
        print('Желаете продолжить нажмите Enter: ')
        cont = input()
        if cont.lower() == 'д' or cont.lower() == 'y':
            break
        else:
            continue
