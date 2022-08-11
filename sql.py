import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()

print('Wat do you want?')
choice = input('Ad member tab N, select member tab S')


def new_member():
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        name text,
        age integer
    )""")
    cur.execute("""INSERT INTO articles VALUES (?, ?)""", (name, age))
    db.commit()


def see_member():
    see_all = input('If you see all tap U: ')
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

db.close()
