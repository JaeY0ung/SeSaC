from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
sung_file_path = "/Users/jeongjaeyeong/Project/SeSac/1.파이썬/src/koreanNames_sung.txt"
irum_file_path = "/Users/jeongjaeyeong/Project/SeSac/1.파이썬/src/koreanNames_irum.txt"

def fileread(file_path):
    with open(file_path, "r") as file:  
        data = file.read().splitlines()  # 여러줄을 가져와서 line으로 쪼개기
        return data

@app.route('/')
@app.route('/<name>')
def home():
    users = [
        {'name': 'Alice', 'age':25, 'phone': '123-456-7890'},
        {'name': 'Bob', 'age':30, 'phone':'312-645-8567'},
        {'name': 'Charlie', 'age':35, 'phone':'123-098-7654'}
    ]
    return render_template("index3.html", username = users)

@app.route('/login')
def login():
    return render_template("login.html")

if __name__  == "__main__":
    app.run(port=8080) # debug=True 하면 오류시 디버그화면이 뜬다.