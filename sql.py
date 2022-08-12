import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()

print('Wat do you want?')
choice = input('Ad member tab N: \n see member tab S: \n update age memeber tab U:  ')
cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        name text PRIMARY KEY,
        age integer
    )""")


def new_member():
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    cur.execute("""INSERT INTO articles VALUES (?, ?)""", (name, age))
    db.commit()


def update_age():
    name = input('Введите имя: ')
    age = input('Какой возраст ввести: ')
    cur.execute(f"""UPDATE articles SET age = '{age}' WHERE name = '{name}'""")
    db.commit()


def see_member():
    see_all = input('If you see all tap Y: ')
    if see_all.lower() == 'u':
        cur.execute("SELECT name FROM articles")
        one_result = cur.fetchall()
        for i in one_result:
            d = ''
            f = d.join(i)
            print(f, end=', ')


if choice.lower() == 'n':
    new_member()
elif choice.lower() == 's':
    see_member()
elif choice.lower() == 'u':
    update_age()

db.close()
