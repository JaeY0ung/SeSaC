import sqlite3

# DB 접속   
conn = sqlite3.connect("hello.db")

# Conn을 통해서 메시지를 주고 받음
# 로우 레벨 접속을 한 소켓 인터페이스
# 깜빡거리는(터미널:흰색박스) 커서(명령어를 주고받는 위치)

# c: 커서
c = conn.cursor()
user_input = 'user1'
pass_input = 'abcd1111'
c.execute("SELECT * FROM users WHERE username=? AND password=?",
          (user_input, pass_input))
result = c.fetchall()
# c.fetchone

# 로그인 기능 구현
if len(result):
    print("login 성공")
else:
    print("login 실패")

for r in result:
    print(r)


# DB 사용이 끝났을 때 변경사항들을 최종적으로 가록
conn.commit()

# 접속을 종료
conn.close()