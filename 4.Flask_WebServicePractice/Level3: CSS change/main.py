from flask import Flask, render_template, request
import csv
import math

def fileread(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for row in rdr:
            clean_row = [element.strip() for element in row]
            data.append(clean_row)
    return data

app = Flask(__name__)

@app.route('/')
@app.route('/users')
def users_info():
    data = fileread("src/user_many.csv")
    headers = [header.strip() for header in data[0]]
    users = data[1:]
    page = request.args.get('page', default=1,  type=int)
    id   = request.args.get('id'  , default="", type=str)
    search_user = request.args.get('search_user', default="", type=str)

    if search_user != "":
        users = [user for user in users if search_user in user[1]]

    if id != "":
        userdata = [user for user in users if id == user[0]]
        return render_template("click_userid.html", headers = headers, 
                               userdata = userdata, username = users[0][1], page = page, search_user=search_user)
    
    per_page = 10 # 한 페이지에 보이는 정보의 개수
    user_num = len(users)
    total_page = math.ceil(user_num / per_page) # 총 페이지 개수
    start_index = (page-1) * per_page # 그 페이지의 첫번째 유저 정보가 users의 몇번째 인덱스인지

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = (page) * per_page - 1 #전체 페이지
    else:
        end_index = user_num - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보 (총 5개 나옴/ 기본은 가운데에 지금 페이지!)
    if page < 3:
        start_page = 1
        end_page   = min(5, total_page)
    elif page <= total_page - 2:
        start_page = page - 2
        end_page   = page + 2
    else:
        start_page = total_page - 4
        end_page  = total_page
    
    return render_template("users.html", headers=headers, 
                           users=users[start_index : end_index + 1], page=page, 
                           total_page=total_page, start_page=start_page, end_page=end_page, search_user=search_user)

@app.route('/orders')
def orders_info():
    data = fileread("src/order.csv")
    headers = [header.strip() for header in data[0]]
    orders = data[1:]
    page = request.args.get('page', default=1,  type=int)
    id   = request.args.get('id'  , default="", type=str)
    search_order = request.args.get('search_order', default="", type=str)

    if search_order != "":
        orders = [order for order in orders if search_order in order[1]]

    if id != "":
        orderdata = [order for order in orders if id == order[0]]
        return render_template("click_orderid.html", headers = headers, 
                               orderdata = orderdata, ordername = orders[0][1], page = page, search_order=search_order)
    
    per_page = 10 # 한 페이지에 보이는 정보의 개수
    order_num = len(orders)
    total_page = math.ceil(order_num / per_page) # 총 페이지 개수
    start_index = (page-1) * per_page # 그 페이지의 첫번째 유저 정보가 orders의 몇번째 인덱스인지

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = (page) * per_page - 1 #전체 페이지
    else:
        end_index = order_num - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보 (총 5개 나옴/ 기본은 가운데에 지금 페이지!)
    if page < 3:
        start_page = 1
        end_page   = min(5, total_page)
    elif page <= total_page - 2:
        start_page = page - 2
        end_page   = page + 2
    else:
        start_page = total_page - 4
        end_page  = total_page
    
    return render_template("orders.html", headers=headers, 
                           orders=orders[start_index : end_index + 1], page=page, 
                           total_page=total_page, start_page=start_page, end_page=end_page, search_order=search_order)


@app.route('/orderitems')
def orderitems_info():
    pass
@app.route('/items')
def items_info():
    pass
@app.route('/stores')
def stores_info():
    pass

if __name__  == "__main__":
    app.run(port=8080, debug=True)