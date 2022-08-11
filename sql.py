import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS articles(
    name text,
    age integer
)""")

# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
#
# cur.execute("""INSERT INTO articles VALUES (?, ?)""", (name, age))
cur.execute("SELECT name FROM articles")
one_result = cur.fetchall()
name_list = []
for i in one_result:
    d = ''
    f = d.join(i)
    name_list.append(f)
    print(f)

print(name_list)


db.commit()


db.close()
