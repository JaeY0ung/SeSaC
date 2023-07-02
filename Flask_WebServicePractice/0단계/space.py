from flask import Flask, redirect, url_for, render_template, request
import csv

def fileread(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for row in rdr:
            clean_row = [element.strip() for element in row]
            data.append(clean_row)
    return data

data = fileread("src/data_space.csv")
userdatatype = [header.strip() for header in data[0]]
users = data[1:]

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def home():
    return render_template("index4.html", users = users, userdatatype = userdatatype)

@app.route('/user/<name>', methods=['GET','POST'])
def user(name):
    userdata = request.form
    # userdata = ["0a497257-2b1a-4836-940f-7b95db952e61", "강준영", "Male", "28", "1994-09-08", "대구 강서구 59길 66"]
    return render_template("index5.html", name = name, userdatatype = userdatatype, userdata = userdata)

if __name__  == "__main__":
    app.run(port=8080)