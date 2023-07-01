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
    usernames = []
    for i in fileread(sung_file_path):
        for j in fileread(irum_file_path):
            usernames.append(i+j)
    return render_template("index.html", username = usernames)

@app.route('/login')
def login():
    return render_template("login.html")

if __name__  == "__main__":
    app.run(port=8080) # debug=True 하면 오류시 디버그화면이 뜬다.