from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import sqlite3

bot = Bot(token="1521325076:AAFfDO4zU6ZQcN1HxaUh1y6BNtkGYLEDvzs")
# Диспетчер для бота
dp = Dispatcher(bot)

db = sqlite3.connect('base.db')
cur = db.cursor()


@dp.message_handler(commands=['start'])
async def start_up(message: types.Message):
    await message.answer('Що плануєтет робити?')
    await message.answer('Ad member tab N: \nSee member tab S: \nUpdate age memeber tab U: \nDelete user tab D: ')

# cur.execute("""CREATE TABLE IF NOT EXISTS articles(
#         name text PRIMARY KEY,
#         age text
#     )""")

def new_member():
    try:
        name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        cur.execute("""INSERT INTO articles VALUES (?, ?)""", (name, age))
        db.commit()
    except:
        print('Такое имя уже есть попробуй другое')
        new_member()


def update_age():
    name = input('Введите имя: ')
    age = input('Какой возраст ввести: ')
    cur.execute(f"""UPDATE articles SET age = '{age}' WHERE name = '{name}'""")
    db.commit()


def see_member():
    see_user = input('Если хотите увидеть всех нажмите Y. Если хотите увидеть отдельного персонажа нажмите О.')
    if see_user.lower() == 'y':
        cur.execute("SELECT name FROM articles")
        one_result = cur.fetchall()
        for i in one_result:
            d = ''
            print(d.join(i), end=', ')
    elif see_user.lower() == 'o':
        name = input('Введите имя: ')
        templates = ''
        print(name, 'age is',
              templates.join(cur.execute(f"""SELECT age FROM articles WHERE name = '{name}'""").fetchone()))


def delete_user():
    name = input('Введите имя: ')
    cur.execute(f"""DELETE FROM articles WHERE name = '{name}'""")
    db.commit()


# if choice.lower() == 'n':
#     new_member()
# elif choice.lower() == 's':
#     see_member()
# elif choice.lower() == 'u':
#     update_age()
# elif choice.lower() == 'd':
#     delete_user()

db.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
