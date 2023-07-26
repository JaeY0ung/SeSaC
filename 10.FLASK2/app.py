from flask import Flask, request, render_template, url_for, redirect, session, flash
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/', methods=["GET","POST"])
def home():
    flash('메세지 테스트')
    if request.method == "GET":
        name = request.args.get('name', default='', type=str )
        # age = request.args.get('age', default=0, type=int)
    elif request.method == "POST":
        name = request.form['name']
        # session.permanent = True
        #? 세션 안에 저장
        session['userid'] = name
        flash('Login에 성공했습니다.')
    else:
        return "UNKNOWN METHOD"
    return render_template('index.html', name = name)

@app.route('/redirect')
def redirect_2():
    return redirect('/')

@app.route('/user')
def user():
    if "userid" in session:
        user = session["userid"]
        return f"<h1>Hello, {user}"
    else:
        return redirect(url_for("home"))

if __name__== '__main__':
    app.debug=True
    app.run(port=8080)