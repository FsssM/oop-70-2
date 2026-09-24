import sqlite3

# Подключаемся к БД кинотеатра
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# Включение поддержки внешних ключей (FOREIGN KEY) в SQLite
cursor.execute('PRAGMA foreign_keys = ON;')


#Создание таблиц и данные

# 1. Таблица пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# 2. Таблица фильмов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
''')

# 3. Таблица отзывов (связующая)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 10),
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
    )
''')

conn.commit()


# Функция заполнения тестовыми данными (чтобы не дублировать при повторном запуске)
def populate_data():
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        # Добавляем 5 пользователей
        users = [('Алихан',), ('Бексултан',), ('Диана',), ('Эльдар',), ('София',)]
        cursor.executemany('INSERT INTO users (name) VALUES (?)', users)

        # Добавляем 5 фильмов (пятый без отзывов для проверки LEFT JOIN)
        movies = [
            ('Начало', 'Фантастика'),
            ('Интерстеллар', 'Фантастика'),
            ('Темный рыцарь', 'Боевик'),
            ('Побег из Шоушенка', 'Драма'),
            ('Аватар 3', 'Фантастика')
        ]
        cursor.executemany('INSERT INTO movies (title, genre) VALUES (?, ?)', movies)

        #10 отзывов (user_id, movie_id, rating)
        reviews = [
            (1, 1, 9),   # Алихан -> Начало (9)
            (1, 2, 10),  # Алихан -> Интерстеллар (10)
            (2, 1, 8),   # Бексултан -> Начало (8)
            (2, 3, 10),  # Бексултан -> Темный рыцарь (10)
            (3, 2, 9),   # Диана -> Интерстеллар (9)
            (3, 4, 10),  # Диана -> Побег из Шоушенка (10)
            (4, 3, 7),   # Эльдар -> Темный рыцарь (7)
            (4, 4, 8),   # Эльдар -> Побег из Шоушенка (8)
            (5, 1, 10),  # София -> Начало (10)
            (5, 2, 8)    # София -> Интерстеллар (8)
        ]
        cursor.executemany('INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)', reviews)
        conn.commit()


# Заполняем базу
populate_data()


# 2 часть

print("=== 1. Имя пользователя + Фильм + Оценка (INNER JOIN) ===")
cursor.execute('''
    SELECT users.name, movies.title, reviews.rating
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
''')
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: {row[1]} | Оценка: {row[2]}")

print("\n=== 2. ВСЕ фильмы, даже без отзывов (LEFT JOIN) ===")
cursor.execute('''
    SELECT movies.title, reviews.rating
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
''')
for row in cursor.fetchall():
    rating_str = row[1] if row[1] is not None else "Нет отзывов"
    print(f"Фильм: {row[0]} | Оценка: {rating_str}")


#3ч агрегации

print("\n=== Статистика оценок по всем фильмам ===")
cursor.execute('''
    SELECT 
        AVG(rating) AS avg_rating,
        MAX(rating) AS max_rating,
        MIN(rating) AS min_rating
    FROM reviews
''')
stats = cursor.fetchone()
print(f"Средняя оценка: {round(stats[0], 2) if stats[0] else 0}")
print(f"Максимальная оценка: {stats[1]}")
print(f"Минимальная оценка: {stats[2]}")

# Закрываем соединение
conn.close()