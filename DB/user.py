import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')






# # 몇 명의 사용자 추가
# users = [
#     ('John Doe', 25, 'Male'),
#     ('Jane Smith', 30, 'Female'),
#     ('Michael Johnson', 35, 'Male'),
#     ('Emily Davis', 28, 'Female'),
#     ('David Lee', 32, 'Male'),
#     ('Emma Wilson', 27, 'Female'),
#     ('Daniel Brown', 31, 'Male'),
#     ('Olivia Taylor', 29, 'Female'),
#     ('Sophia Anderson', 33, 'Female'),
#     ('Matthew Martin', 26, 'Male')
# ]
# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# # 변경사항 저장
# conn.commit()


# 성별:여자
cursor.execute("SELECT * FROM users WHERE gender='Female'")
result = cursor.fetchall()
print("여자 고객 목록:")
for r in result:
    print(r)

# 나이가 30이상
cursor.execute("SELECT * FROM users WHERE age >= 30")
result = cursor.fetchall()
print("나이>=30 고객 목록:")
for r in result:
    print(r)

# 나이가 25세 이상 30세 이하
cursor.execute("SELECT * FROM users WHERE age >= 25 AND age <=30")
result = cursor.fetchall()
print("25<=나이<=30 고객 목록:")
for r in result:
    print(r)

# 성별 그룹핑
cursor.execute("SELECT gender, COUNT(*) FROM users GROUP BY gender")
result = cursor.fetchall()
print("남/여 고객 목록:")
for gender,count in result:
    print(f"{gender}: {count}")


# 미션5: John 나이 25 -> 26
cursor.execute("UPDATE users SET age=26 WHERE name='John Doe'")
conn.commit() # 변동사항이 있으면 최종 변경사항이후 commit해야 한다. (UPDATE DELETE 등)
cursor.execute("SELECT * FROM users WHERE name='John Doe'")
result = cursor.fetchall()
print(result)


# 미션6: Emily 사용자 삭제
cursor.execute("DELETE FROM users WHERE name='Emily Davis'")
conn.commit() # 변동사항이 있으면 최종 변경사항이후 commit해야 한다. (UPDATE DELETE 등)
cursor.execute("SELECT * FROM users WHERE name='Emily Davis'")
result = cursor.fetchall()

conn.close()