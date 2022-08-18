import random
import time

random_num = random.randint(1, 100)

def game():
    while True:
        try:
            user_num = int(input('Угадай число от 1 до 100.\nВведи число: '))
            if user_num == random_num:
                print('Ура победа')
                time.sleep(2)
                break
            elif user_num > random_num:
                print('Число больлше чем задуманое')
            else:
                print('Число меньше чем задуманое')
        except:
            print('Нужно ввести число!!!')



game()