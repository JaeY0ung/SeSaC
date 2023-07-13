from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/user')
def user_none():
    return """
    <UL>
    <LI> <a href="/user/tom">tom</a> </LI>
    <LI> <a href="/user/john">john</a> </LI>
    <LI> <a href="/user/bill">bill</a> </LI>
"""

@app.route('/user/<name>')
def user(name):
    return f"""
    <H1>This is{name}'s Homepage</H1>
    <a href="/">Go Back</a>"""

@app.route('/admin')
def admin():
    return redirect(url_for('user', name="admin"))
if __name__  == "__main__":
    app.run(port= 5000)