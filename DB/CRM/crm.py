import sqlite3

# 초기 설정
conn = sqlite3.connect("./crm.db")
# cursor
cursor = conn.cursor()

# conn.commit()

# users 테이블 삭제
cursor.execute('DROP TABLE users;')
conn.commit()

# users2 테이블 삭제
cursor.execute('DROP TABLE users2;')
conn.commit()

# csv파일 테이블로 가져오기
cursor.execute('.mode csv')
cursor.execute('.import crm_user.csv users')

conn.commit()

# 테이블 없을 때만 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users2(
               "id" INTEGER PRIMARY KEY AUTOINCREMENT,
               "userid" TEXT,
               "username" TEXT,
               "userbirthday" TEXT,
               "usergender" TEXT,
               "userage" INTEGER,
               "useraddress" TEXT);
               ''')
conn.commit()

cursor.execute('''INSERT INTO users2(userid, username, userbirthday, usergender, userage, useraddress) 
SELECT userid, username, userbirthday, usergender, userage, useraddress FROM users;''')
conn.commit()

conn.close()
