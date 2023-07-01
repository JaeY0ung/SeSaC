from flask import Flask, redirect, url_for, render_template
import csv

app = Flask(__name__)

file_path = "src/user.csv"

def fileread(file_path):
    data = []
    f = open(file_path, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for i in rdr:
        data.append(i)
    return data

@app.route('/') 
def home():
    data = fileread(file_path)
    userdatatype = data[0]
    users = data[1:]
    return render_template("index4.html", users = users, userdatatype = userdatatype)

if __name__  == "__main__":
    app.run(port=8080) # debug=True 하면 오류시 디버그화면이 뜬다.