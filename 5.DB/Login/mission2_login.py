import sqlite3
import hashlib
# 데이터베이스 연결
conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# 존재하는 테이블 없애기
def tableDestroy():
    cursor.execute("DROP TABLE IF EXISTS logins")
    conn.commit()

# 사용자 테이블 생성
def tableCreate():
    cursor.execute('''CREATE TABLE IF NOT EXISTS logins
                    (uni_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id TEXT,
                    pwd TEXT)''')
    conn.commit()

# 테이블에 회원가입 정보 입력
def register():
    print("< 회원가입 창 >")
    input_id = input("사용할 id를 입력하세요: ")
    input_pwd = input("사용할 pwd를 입력하세요: ")

    cursor.execute("SELECT * FROM logins WHERE id=?", [input_id])
    result = cursor.fetchall()
    if len(result):
        print("이미 존재하는 아이디입니다.")
        return register()
    
    cursor.execute("INSERT INTO logins(id, pwd) VALUES(?, ?)", [input_id, hash_password(input_pwd)])
    cursor.execute("SELECT * FROM logins")
    result = cursor.fetchall()
    print(f"result = {result}")
    conn.commit()

    print("회원가입이 완료되었습니다.\n")    
    return

def login():
    print("< 로그인 창 >")
    input_id = input("id를 입력하세요: ")
    input_pwd = input("pwd를 입력하세요: ")

    cursor.execute("SELECT * FROM logins WHERE id=? AND pwd=?", [input_id, hash_password(input_pwd)])
    result = cursor.fetchall()
    if len(result) == 1:
        print("로그인 성공\n")
        return
    if input("다시 입력하시겠습니까?(Y/N)").lower() == 'y':
        return login()
    else:
        print("로그인을 종료합니다.\n")
        return
    
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def hashlogin():
    print("< 로그인 창 >")
    input_id = input("id를 입력하세요: ")
    input_pwd = input("pwd를 입력하세요: ")

    cursor.execute("SELECT * FROM logins WHERE id=? AND pwd=?", [input_id, input_pwd])
    result = cursor.fetchall()
    if len(result) == 1:
        print("로그인 성공\n")
        return
    if input("다시 입력하시겠습니까?(Y/N)").lower() == 'y':
        return login()
    else:
        print("로그인을 종료합니다.\n")
        return

# 테이블 보여주기
def showAll():
    cursor.execute("SELECT * FROM logins")
    results = cursor.fetchall()
    for result in results:
        print(result)
    return


tableDestroy()
tableCreate()
if input("회원가입을 하시겠습니까? (Y/N)").lower() == "y":
    register()
if input("로그인을 하시겠습니까? (Y/N)").lower() == "y":
    login()

showAll()
conn.close()

# md5
# sha256/512