from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination
import sqlite3

user_bp = Blueprint('user', __name__)

conn = sqlite3.connect('crm.db')
cursor = conn.cursor()
query = ''
cursor.execute(query)
datas = cursor.fetchall()

@user_bp.route('/users')
def users_info():
    file_rdr = File()
    data     = file_rdr.read("./csv/crm_user.csv")

    headers = [header.strip() for header in data[0]]
    users   = data[1:]

    page          = request.args.get('page',          default=1,  type=int)
    id            = request.args.get('id'  ,          default="", type=str)
    search_user   = request.args.get('search_user',   default="", type=str)
    choice_gender = request.args.get('choice_gender', default="", type=str)

    highlight_index = [[0,0] for _ in users]

    # 검색창에 user 검색시
    if search_user:
        # users 갱신
        users = [user for user in users if search_user in user[1]]
        highlight_index = []
        for user in users:
            name = user[1]
            l = len(search_user)
            for i in range(len(name) - l + 1):
                if search_user == name[i : i + l]:
                    highlight_index.append( (i, i + l - 1) )
                    print(highlight_index)
                    break

    if choice_gender: # gender select filter 
        users = [user for user in users if choice_gender == user[3]]

    if id: # click id
        userdata = [user for user in users if id == user[0]]
        return render_template("click_userid.html", headers = headers, 
                               userdata = userdata, username = users[0][1], 
                               page = page, search_user=search_user)
    
    
    pagemaker = Pagination()
    pagemaker.makepagination(users, page)

    start_index = pagemaker.start_index
    end_index = pagemaker.end_index
    total_page = pagemaker.total_page
    pagination_start = pagemaker.pagination_start
    pagination_end = pagemaker.pagination_end
    move_page_front = pagemaker.move_page_front
    move_page_back = pagemaker.move_page_back
    
    return render_template("users.html",
                           headers=headers, users=users[start_index : end_index + 1],
                           page=page, total_page=total_page,
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_user=search_user, choice_gender=choice_gender, highlight_index=highlight_index)