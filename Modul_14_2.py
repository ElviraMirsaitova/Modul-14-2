import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#решение будет после этого закомменченного блока
#____________________________________________________________________________________________________________
#создание записей

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

#обновление данных записей

# for i in range(10):
#     if (i+1) % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i+1))

#удаление записей

# count = 0
# while count < 10:
#     cursor.execute('DELETE FROM Users WHERE id = ?', (count+1,))
#     count = count + 3

# cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст:{user[2]} | Баланс: {user[3]}')

# cursor.execute(" SELECT COUNT (*) FROM Users")
# users = cursor.fetchall()

# connection.commit()
# connection.close()
#__________________________________________________________________________________________________________________

# Удаление пользователя с id=6

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute(" SELECT COUNT (*) FROM Users")
total_users = cursor.fetchone()[0]


# Подсчёт суммы всех балансов
cursor.execute(" SELECT SUM (balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)
connection.close()


