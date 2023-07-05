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
def main():
    return render_template('home.html')

@app.route('/users')
def users_info():
    data = fileread("src/user.csv")
    headers = [header.strip() for header in data[0]]
    users = data[1:]
    page          = request.args.get('page',          default=1,  type=int)
    id            = request.args.get('id'  ,          default="", type=str)
    search_user   = request.args.get('search_user',   default="", type=str)
    choice_gender = request.args.get('choice_gender', default="", type=str)

    if search_user:
        users = [user for user in users if search_user in user[1]]
    if choice_gender:
        users = [user for user in users if choice_gender == user[2]]
    if id:
        userdata = [user for user in users if id == user[0]]
        return render_template("click_userid.html", headers = headers, 
                               userdata = userdata, username = users[0][1], 
                               page = page, search_user=search_user)

    data_per_page = 10 # 한 페이지에 보이는 data 개수
    page_per_pagination = 5 # 홀수/ pagination에 보아는 page수
    num_data = len(users) # data에 있는 정보의 개수
    total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
    start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = page * data_per_page - 1 #전체 페이지
    else:
        end_index = num_data - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
    if total_page >= page_per_pagination:
        if page <= 1+ page_per_pagination//2:
            pagination_start, pagination_end = 1, page_per_pagination
            move_page_front, move_page_back = False, True
        elif page <= total_page - page_per_pagination//2:
            pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
            move_page_front, move_page_back = True, True
        else:
            pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
            move_page_front, move_page_back = True, False

    else:
        pagination_start, pagination_end = 1, total_page
        move_page_front, move_page_back = False, False

    return render_template("users.html", headers=headers, 
                           users=users[start_index : end_index + 1], page=page, 
                           total_page=total_page, pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_user=search_user, choice_gender=choice_gender)

@app.route('/orders')
def orders_info():
    data = fileread("src/order.csv")
    headers = [header.strip() for header in data[0]]
    orders  = data[1:]
    page         = request.args.get('page',         default=1,  type=int)
    id           = request.args.get('id'  ,         default="", type=str)
    search_order = request.args.get('search_order', default="", type=str)
    choice_year  = request.args.get('choice_year',  default="", type=str)
    choice_month = request.args.get('choice_month', default="", type=str)
    choice_day   = request.args.get('choice_day',   default="", type=str)
    
    if search_order:
        orders = [order for order in orders if search_order in order[0]]
    if choice_year:
        orders = [order for order in orders if choice_year == order[1][0:4]]
    if choice_month:
        orders = [order for order in orders if choice_month == order[1][5:7]]
    if choice_day:
        orders = [order for order in orders if choice_day == order[1][8:10]]
    if id:
        orderdata = [order for order in orders if id == order[0]]
        return render_template("click_orderid.html", headers = headers, 
                               orderdata = orderdata, orderat = orders[0][1], page = page, search_order=search_order)
    
    data_per_page = 10 # 한 페이지에 보이는 data 개수
    page_per_pagination = 5 # 홀수/ pagination에 보아는 page수
    num_data = len(orders) # data에 있는 정보의 개수
    total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
    start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = page * data_per_page - 1 #전체 페이지
    else:
        end_index = num_data - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
    if total_page >= page_per_pagination:
        if page <= 1+ page_per_pagination//2:
            pagination_start, pagination_end = 1, page_per_pagination
            move_page_front, move_page_back = False, True
        elif page <= total_page - page_per_pagination//2:
            pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
            move_page_front, move_page_back = True, True
        else:
            pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
            move_page_front, move_page_back = True, False

    else:
        pagination_start, pagination_end = 1, total_page
        move_page_front, move_page_back = False, False
    
    return render_template("orders.html", headers=headers, 
                           orders=orders[start_index : end_index + 1], page=page, 
                           total_page=total_page, pagination_start=pagination_start, 
                           pagination_end=pagination_end, search_order=search_order,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           choice_year=choice_year, choice_month=choice_month, choice_day=choice_day)


@app.route('/orderitems')
def orderitems_info():
    data = fileread("src/orderitem.csv")
    headers = [header.strip() for header in data[0]]
    orderitems = data[1:]
    page = request.args.get('page', default=1,  type=int)
    id   = request.args.get('id'  , default="", type=str)
    search_orderitem = request.args.get('search_orderitem', default="", type=str)

    if search_orderitem:
        orderitems = [orderitem for orderitem in orderitems if search_orderitem in orderitem[0]]

    if id:
        orderitemdata = [orderitem for orderitem in orderitems if id == orderitem[0]] # else break; 가능?
        return render_template("click_orderitemid.html", headers = headers, 
                               orderitemdata = orderitemdata, orderitemname = orderitems[0][0], 
                               page = page, search_orderitem=search_orderitem)
    
    data_per_page = 10 # 한 페이지에 보이는 data 개수
    page_per_pagination = 5 # 홀수/ pagination에 보아는 page수
    num_data = len(orderitems) # data에 있는 정보의 개수
    total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
    start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = page * data_per_page - 1 #전체 페이지
    else:
        end_index = num_data - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
    if total_page >= page_per_pagination:
        if page <= 1+ page_per_pagination//2:
            pagination_start, pagination_end = 1, page_per_pagination
            move_page_front, move_page_back = False, True
        elif page <= total_page - page_per_pagination//2:
            pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
            move_page_front, move_page_back = True, True
        else:
            pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
            move_page_front, move_page_back = True, False

    else:
        pagination_start, pagination_end = 1, total_page
        move_page_front, move_page_back = False, False
    
    return render_template("orderitems.html", headers=headers, 
                           orderitems=orderitems[start_index : end_index + 1], page=page, 
                           total_page=total_page, pagination_start=pagination_start, 
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           pagination_end=pagination_end, search_orderitem=search_orderitem)


@app.route('/items')
def items_info():
    data = fileread("src/item.csv")
    headers = [header.strip() for header in data[0]]
    items = data[1:]
    page        = request.args.get('page', default=1,  type=int)
    id          = request.args.get('id'  , default="", type=str)
    search_item = request.args.get('search_item', default="", type=str)
    choice_type = request.args.get('choice_type', default="", type=str)
    if search_item:
        items = [item for item in items if search_item in item[0]]
    if choice_type:
        items = [item for item in items if choice_type == item[2]]
    if id:
        itemdata = [item for item in items if id == item[0]]
        return render_template("click_itemid.html", headers = headers, 
                               itemdata = itemdata, itemname = items[0][0], 
                               page = page, search_item=search_item)
    
    data_per_page = 10 # 한 페이지에 보이는 data 개수
    page_per_pagination = 5 # 홀수/ pagination에 보아는 page수
    num_data = len(items) # data에 있는 정보의 개수
    total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
    start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = page * data_per_page - 1 #전체 페이지
    else:
        end_index = num_data - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
    if total_page >= page_per_pagination:
        if page <= 1+ page_per_pagination//2:
            pagination_start, pagination_end = 1, page_per_pagination
            move_page_front, move_page_back = False, True
        elif page <= total_page - page_per_pagination//2:
            pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
            move_page_front, move_page_back = True, True
        else:
            pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
            move_page_front, move_page_back = True, False

    else:
        pagination_start, pagination_end = 1, total_page
        move_page_front, move_page_back = False, False
    
    return render_template("items.html", headers=headers, 
                           items=items[start_index : end_index + 1], page=page, 
                           total_page=total_page, pagination_start=pagination_start, 
                           pagination_end=pagination_end, search_item=search_item,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           choice_type=choice_type)


@app.route('/stores')
def stores_info():
    data = fileread("src/store.csv")
    headers = [header.strip() for header in data[0]]
    stores = data[1:]
    page = request.args.get('page', default=1,  type=int)
    id   = request.args.get('id'  , default="", type=str)
    search_store = request.args.get('search_store', default="", type=str)
    choice_type = request.args.get('choice_type', default="", type=str)

    if search_store:
        stores = [store for store in stores if search_store in store[1]]
    if choice_type:
        stores = [store for store in stores if choice_type == store[2]]
    if id:
        storedata = [store for store in stores if id == store[0]]
        return render_template("click_storeid.html", headers = headers, 
                               storedata = storedata, storename = stores[0][1],
                               page = page, search_store=search_store)
    
    data_per_page = 10 # 한 페이지에 보이는 data 개수
    page_per_pagination = 5 # 홀수/ pagination에 보아는 page수
    num_data = len(stores) # data에 있는 정보의 개수
    total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
    start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

    # 페이지에 따른 마지막 정보의 index값
    if page < total_page:
        end_index = page * data_per_page - 1 #전체 페이지
    else:
        end_index = num_data - 1

    # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
    if total_page >= page_per_pagination:
        if page <= 1+ page_per_pagination//2:
            pagination_start, pagination_end = 1, page_per_pagination
            move_page_front, move_page_back = False, True
        elif page <= total_page - page_per_pagination//2:
            pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
            move_page_front, move_page_back = True, True
        else:
            pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
            move_page_front, move_page_back = True, False

    else:
        pagination_start, pagination_end = 1, total_page
        move_page_front, move_page_back = False, False

    return render_template("stores.html", headers=headers, 
                           stores=stores[start_index : end_index + 1], page=page, 
                           total_page=total_page, pagination_start=pagination_start,
                           pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_store=search_store, choice_type=choice_type)

if __name__  == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)