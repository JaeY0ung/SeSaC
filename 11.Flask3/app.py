from flask import Flask, redirect, render_template, request, session, url_for, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'this_is_my_secret_key'
app.permanent_session_lifetime = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI'] =

users = {
    'user1':{'password': 'password123'},
    'user2':{'password': 'password456'},
    'hanol987':{'password': '980529'}
}

@app.route('/')
def home():
    username = None
    if 'username' in session:
        username = session['username']
    return render_template('home.html', username = username)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            flash('로그인 성공', 'success')
            return redirect(url_for('home'))
        else:
            flash('로그인 실패', 'danger')
            # return 'INVALID USERNAME or PASSWORD. PLEASE TRY AGAIN'
    return render_template('login.html')


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        flash('로그아웃', 'success')
    else:
        flash('아무일도 안 일어남', 'success')
    return redirect(url_for('home'))
 
if __name__ == '__main__':
    app.run(port=8080, debug= True)

#? 미션1: 렌더템플릿 통해서 첫화면에 login/logout 추가 (부트스트랩 nav통해서 - 메뉴에 login.logout 넣기)
#? 미션2: 로그인 성공 실패 여부를 flash 메시지 통해서 처리
#? 미션3: 디자인 적용해서 flash 메세지 색상 다르게 해보기 (성공시 초록, 실패시 빨강)