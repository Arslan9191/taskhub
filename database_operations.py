import sqlite3

# Указываем точное расположение файла базы данных
db_path = r"C:\Users\Arslan\Documents\taskhub\taskhub.db"

# Создаем соединение с базой данных (если ее нет, то она будет создана)
conn = sqlite3.connect(db_path)

# Создаем объект курсора, который мы будем использовать для выполнения SQL-запросов
cur = conn.cursor()

# Создаем таблицу пользователей
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')

# Создаем таблицу задач, добавляем поле deadline
cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                deadline DATETIME NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )''')

# Создаем таблицу откликов с полем acceptance_time
cur.execute('''CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY,
                task_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                response_text TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending',
                acceptance_time DATETIME,
                FOREIGN KEY (task_id) REFERENCES tasks(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS chat (
                id INTEGER PRIMARY KEY,
                task_id INTEGER NOT NULL,
                sender_id INTEGER NOT NULL,
                receiver_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME NOT NULL,
                FOREIGN KEY (task_id) REFERENCES tasks(id),
                FOREIGN KEY (sender_id) REFERENCES users(id),
                FOREIGN KEY (receiver_id) REFERENCES users(id)
            )''')

# Проверяем и добавляем недостающую колонку acceptance_time, если она отсутствует
cur.execute("PRAGMA table_info(responses)")
columns = [column[1] for column in cur.fetchall()]
if 'acceptance_time' not in columns:
    cur.execute("ALTER TABLE responses ADD COLUMN acceptance_time DATETIME")
    
cur.execute("PRAGMA table_info(tasks)")
columns = [column[1] for column in cur.fetchall()]
if 'creation_time' not in columns:
    cur.execute("ALTER TABLE tasks ADD COLUMN creation_time DATETIME")
    
cur.execute("PRAGMA table_info(responses)")
columns = [column[1] for column in cur.fetchall()]
if 'report_text' not in columns:
    cur.execute("ALTER TABLE responses ADD COLUMN report_text TEXT")

cur.execute("PRAGMA table_info(responses)")
columns = [column[1] for column in cur.fetchall()]
if 'report_text' not in columns:
    cur.execute("ALTER TABLE responses ADD COLUMN report_text TEXT")
if 'submission_time' not in columns:
    cur.execute("ALTER TABLE responses ADD COLUMN submission_time DATETIME")

cur.execute("PRAGMA table_info(tasks)")
columns = [column[1] for column in cur.fetchall()]
if 'completion_time' not in columns:
    cur.execute("ALTER TABLE tasks ADD COLUMN completion_time DATETIME")

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()
