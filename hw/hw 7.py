import sqlite3

# 1. Подключаемся к базе данных (если файла store.db нет, Python создаст его сам)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# 2. Создаем таблицу products, если она еще не создана
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
conn.commit()


#CRUD ОПЕРАЦИИ

#CREATE — Добавление товара
def create_product(name, price, quantity):
    cursor.execute('''
        INSERT INTO products (name, price, quantity)
        VALUES (?, ?, ?)
    ''', (name, price, quantity))
    conn.commit()
    print(f"Товар '{name}' успешно добавлен!")


#READ — Получение всех товаров
def read_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print("\n--- СПИСОК ТОВАРОВ ---")
    if not products:
        print("База данных пуста.")
    else:
        for product in products:
            # product[0] = id, product[1] = name, product[2] = price, product[3] = quantity
            print(f"ID: {product[0]} | Название: {product[1]} | Цена: {product[2]} сом | Количество: {product[3]} шт.")
    print("----------------------\n")


#UPDATE — Обновление цены товара по ID
def update_product(id, price):
    cursor.execute('''
        UPDATE products 
        SET price = ? 
        WHERE id = ?
    ''', (price, id))
    conn.commit()
    print(f"Цена товара с ID {id} обновлена на {price}!")


#DELETE — Удаление товара по ID
def delete_product(id):
    cursor.execute('''
        DELETE FROM products 
        WHERE id = ?
    ''', (id,))
    conn.commit()
    print(f"Товар с ID {id} успешно удален!")


#ПРОВЕРКА РАБОТЫ ПРОГРАММЫ
if __name__ == '__main__':
    # 1. Добавляем тестовые товары (CREATE)
    create_product("Яблоки", 120.5, 50)
    create_product("Молоко", 80.0, 20)
    create_product("Хлеб", 35.0, 100)

    # 2. Смотрим все товары
    read_products()

    # 3. Обновляем цену у Яблок (ID 1) на 140 сом (UPDATE)
    update_product(1, 140.0)

    # 4. Удаляем Хлеб (ID 3) из базы (DELETE)
    delete_product(3)

    # 5. Проверяем итоговый список
    read_products()

    # Закрываем соединение с базой
    conn.close()