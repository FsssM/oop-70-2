import sqlite3

connect = sqlite3.connect('user_grade.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR(20) NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
''')
connect.commit()


def create_moke_users():
    cursor.executemany(
        'INSERT INTO students(name) VALUES (?)',
        [
            ("ARDAGER",),
            ("ARAZY",),
            ("SLAVA",),
            ("VLAD",),
            ("OLEG",),
        ]
    )
    connect.commit()
    print("Пользователи созданы!!")
# create_moke_users()

def create_moke_grade():
    cursor.executemany(
        'INSERT INTO grades(grade, subject, student_id) VALUES (?, ?, ?)',
        [
            # (5, "Алгерба", 3),
            # (3, "Физра", 4),
            # (2, "Химия", 1),
            # (4, "ФИЗИКА", 5),
            (5, "ИЗО", 2),
        ]
    )
    connect.commit()
    print("Оценки созданы!!")

# create_moke_grade()


def get_student_grade():

    cursor.execute('''
        SELECT students.name, grades.grade, grades.subject
        FROM students FULL OUTER JOIN grades ON students.id = grades.student_id
    ''')
    data = cursor.fetchall()

    # print(data)
    # ('ARDAGER', 2, 'Химия')
    for i in data:
        print(i)
        # print(f"NAME: {i[0]} GRADE: {i[1]} SUBJECT: {i[2]}")


# get_student_grade()



def get_student_hi_grade():

    # MAX() MIN() AVG() COUNT() SUM()
    cursor.execute(
        'SELECT students.name, SUM(grades.grade) FROM students INNER JOIN grades ON students.id = grades.student_id'
    )
    data = cursor.fetchall()
    print(data)

# get_student_hi_grade()

def get_best_students():

    cursor.execute('''
        SELECT name FROM students WHERE id IN (
            SELECT student_id FROM grades
            WHERE grade = 5
            )
    ''')
    data = cursor.fetchall()
    print(data)

# get_best_students()


def create_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
            SELECT students.name, grades.subject, grades.grade
            FROM students INNER JOIN grades ON students.id = grades.student_id
            ORDER BY grades.grade
    ''')
    print('Педставление создано!!')

# create_view()

def get_view_data():
    cursor.execute('SELECT * FROM my_view')
    data = cursor.fetchall()
    print(data)

get_view_data()