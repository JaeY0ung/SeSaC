from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'this_is_my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # 파일위치 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # DB와 자동 동기화 여부 비활성화

db = SQLAlchemy(app)

class Users(db.Model): # Users 테이블 생성
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

@app.route('/')
def home():
    if 'username' in session:
        flash('로그인에 성공하셨습니다.')
        username = session['username']
        return render_template('index.html', username=username)
    
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html', users = Users.query.all())

@app.route('/delete', methods=['POST'])
def delete():
    user = session['username']

    if request.method == 'POST':
        action = request.form['action']
        if action == 'DELETE':
            Users.query.filter_by(name = user).delete()
            db.session.commit()

            return redirect(url_for('logout'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        found_user = Users.query.filter_by(name = username).first()
        if found_user:
            flash('Login Successful')
        else:
            user = Users(username, password, '')
            db.session.add(user) # 사용자 추가
            db.session.commit() 
            flash('User Created')

        session['username'] = username
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context(): # DB 초기화
        db.create_all()
    app.run(port=8080, debug=True)

#? 미션1: 렌더템플릿 통해서 첫화면에 login/logout 추가 (부트스트랩 nav통해서 - 메뉴에 login.logout 넣기)
#? 미션2: 로그인 성공 실패 여부를 flash 메시지 통해서 처리
#? 미션3: 디자인 적용해서 flash 메세지 색상 다르게 해보기 (성공시 초록, 실패시 빨강)