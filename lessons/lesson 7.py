import sqlite3
# Дневник
connect = sqlite3.connect("user.db")
# рука и ручка
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCAHR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD Create-Read-Update-Delete


def create_user(name_t, age_t, hobby_t):
#     cursor.execute(f'''
#     INSERT INTO users( age, name, hobby) VALUES ("{age}", "{name}", "{hobby}")
# ''')

    cursor.execute(
        'INSERT INTO users( age, name, hobby) VALUES (?,?,?)',
    (age_t, name_t, hobby_t)
    )
    connect.commit()
    print('Пользователь добавлен!!')

# create_user("Arzy", 19, "Горы-Лыжи")
# create_user("Slava", 23, "Горы")
# create_user("Ardager", 23, "Горы")
# create_user("MAster", 23, "Горы")

def get_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)
    cursor.execute('SELECT name FROM users')
    data = cursor.fetchall()
    print(data)

# get_users()

def update_user(age, row_id):

    cursor.execute(
        'UPDATE users SET age = ? WHERE rowid = ?',
        (age, row_id)
    )
    connect.commit()
    print("Возраст обнавлен!")

# update_user(100, 2)

def delete_user(row_id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (row_id,)
    )
    connect.commit()
    print("Пользователь удален!!")

# delete_user(2)
input()