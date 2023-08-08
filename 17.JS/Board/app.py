from flask import Flask, render_template, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=["POST"])
def create():
    title = request.form['title']
    message = request.form['message']
    print(f'title: {title}, message: {message}')
    sql = "INSERT INTO board(title, message) VALUES('{}','{}')".format(title, message)
    db.execute(sql)
    db.commit()
    return "OK"

@app.route('/list', methods = ["GET"])
def list():
    sql = "SELECT * FROM board"
    result = db.execute_fetch(sql)
    #? json 형태로 key,value pair로 만들어준다. dict(), zip()
    tuple_keys = ("id", "title","message")
    dict_list = [dict(zip(tuple_keys, r)) for r in result]
    return dict_list
    
@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    sql = "DELETE FROM board WHERE id = '{}'".format(id)
    db.execute(sql)
    db.commit()
    return 'OK'

@app.route('/edit', methods=['POST'])
def edit():
    id = request.form['id']
    edit_title = request.form['edit_title']
    edit_message = request.form['edit_message']

    sql = "UPDATE board SET title='{}', message='{}' WHERE id = '{}'".format(edit_title, edit_message, id)
    db.execute(sql)
    db.commit()
    return 'OK'

if __name__=="__main__":
    app.run(port=8078, debug=True)