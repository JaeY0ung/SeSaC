from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination
import sqlite3

user_bp = Blueprint('user', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@user_bp.route('/users')
def users_info():
    page          = request.args.get('page',          default= 1, type=int)
    click_id      = request.args.get('id'  ,          default="", type=str)
    search        = request.args.get('search',        default="", type=str)
    choice_gender = request.args.get('choice_gender', default="", type=str)

    query = '''SELECT Id, Name, Birthdate, Gender, Age, Address 
               FROM users
               WHERE 1=1
            '''
    if search: 
        #? 중요: like 는 따옴표 써야 한다!
        #? 중요: 공백 있어야 한다!
        query += f" AND Name like '%{search}%'"
    if choice_gender:
        query += f" AND Gender = '{choice_gender}'"
    if click_id: # click id
        query += f" AND Id = '{click_id}'"

    #? 쿼리문 실행
    cursor.execute(query)

    #? crm.db에서 user table의 헤더 가져오기
    headers = [data[0] for data in cursor.description]
    users = cursor.fetchall()

    query2 = f'''SELECT s.Name AS Name, SUM(i.UnitPrice) AS TotalSpend, COUNT(o.Id) AS Count
                FROM users      u
                JOIN orders     o  ON u.id      = o.UserId
                JOIN orderitems oi ON o.Id      = oi.OrderId
                JOIN stores     s  ON o.StoreId = s.Id
                JOIN items      i  ON oi.ItemId = i.Id
                WHERE u.id = '{click_id}'
                GROUP BY o.Id
             '''
    cursor.execute(query2)
    static_headers = [data[0] for data in cursor.description]
    static = cursor.fetchall()
    print(static)

    if click_id:
        return render_template("click_userid.html", headers = headers, 
                               userdata = users[0], page = page, 
                               search = search, static = static, static_headers = static_headers)

    # 검색 단어 하이라이팅
    highlight_index = [[0,0] for _ in users]
    if search:
        highlight_index = []
        for user in users:
            name = user[1]
            l = len(search)
            for i in range(len(name) - l + 1):
                if search == name[i : i + l]:
                    highlight_index.append( (i, i + l - 1) )
                    break

    pagemaker = Pagination()
    pagemaker.makepagination(users, page)
    
    return render_template("users.html",
                           headers=headers, users=users[pagemaker.start_index : pagemaker.end_index + 1],
                           page=page, total_page=pagemaker.total_page,
                           pagination_start=pagemaker.pagination_start, pagination_end=pagemaker.pagination_end,
                           move_page_front=pagemaker.move_page_front, move_page_back=pagemaker.move_page_back,
                           search=search, choice_gender=choice_gender, highlight_index=highlight_index)