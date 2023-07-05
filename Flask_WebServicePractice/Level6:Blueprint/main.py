from flask import Flask, render_template, request
import math
from user.views import user_bp
from File import File
from Pagination import Pagination

app = Flask(__name__)
data_per_page = 10 # 한 페이지에 보이는 data 개수
page_per_pagination = 5 # 홀수/ pagination에 보아는 page수

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/users')
def users_info():
    file_rdr = File()
    data     = file_rdr.read("src/user.csv")

    headers = [header.strip() for header in data[0]]
    users   = data[1:]

    page          = request.args.get('page',          default=1,  type=int)
    id            = request.args.get('id'  ,          default="", type=str)
    search_user   = request.args.get('search_user',   default="", type=str)
    choice_gender = request.args.get('choice_gender', default="", type=str)

    if search_user: # search filter
        users = [user for user in users if search_user in user[1]]
    if choice_gender: # gender select filter 
        users = [user for user in users if choice_gender == user[2]]
    if id: # click id
        userdata = [user for user in users if id == user[0]]
        return render_template("click_userid.html", headers = headers, 
                               userdata = userdata, username = users[0][1], 
                               page = page, search_user=search_user)
    
    pagemaker = Pagination()
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(users, page, data_per_page, page_per_pagination)
    
    return render_template("users.html", headers=headers, users=users[start_index : end_index + 1],
                           page=page, total_page=total_page,
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_user=search_user, choice_gender=choice_gender)

@app.route('/orders')
def orders_info():
    file_rdr = File()
    data     = file_rdr.read("src/order.csv")

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
                               orderdata = orderdata, orderat = orders[0][1],
                               page = page, search_order=search_order)
    
    pagemaker = Pagination()
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(orders, page, data_per_page, page_per_pagination)
    
    return render_template("orders.html", headers=headers, 
                           orders=orders[start_index : end_index + 1], page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end, 
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_order=search_order, choice_year=choice_year, 
                           choice_month=choice_month, choice_day=choice_day)

@app.route('/orderitems')
def orderitems_info():
    file_rdr = File()
    data     = file_rdr.read("src/orderitem.csv")

    headers    = [header.strip() for header in data[0]]
    orderitems = data[1:]

    page             = request.args.get('page',             default=1,  type=int)
    id               = request.args.get('id'  ,             default="", type=str)
    search_orderitem = request.args.get('search_orderitem', default="", type=str)

    if search_orderitem:
        orderitems = [orderitem for orderitem in orderitems if search_orderitem in orderitem[0]]

    if id:
        orderitemdata = [orderitem for orderitem in orderitems if id == orderitem[0]] # else break; 가능?
        return render_template("click_orderitemid.html", headers = headers, 
                               orderitemdata = orderitemdata, orderitemname = orderitems[0][0], 
                               page = page, search_orderitem=search_orderitem)

    pagemaker = Pagination()
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(orderitems, page, data_per_page, page_per_pagination)
    
    return render_template("orderitems.html", headers=headers, 
                           orderitems=orderitems[start_index : end_index + 1], page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_orderitem=search_orderitem)


@app.route('/items')
def items_info():
    file_rdr = File()
    data     = file_rdr.read("src/item.csv")

    headers = [header.strip() for header in data[0]]
    items   = data[1:]

    page        = request.args.get('page',        default=1,  type=int)
    id          = request.args.get('id'  ,        default="", type=str)
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
    
    pagemaker = Pagination()
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(items, page, data_per_page, page_per_pagination)
    
    return render_template("items.html", headers=headers, items=items[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end, 
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_item=search_item, choice_type=choice_type)


@app.route('/stores')
def stores_info():
    file_rdr = File()
    data     = file_rdr.read("src/store.csv")

    headers = [header.strip() for header in data[0]]
    stores  = data[1:]

    page         = request.args.get('page',         default=1,  type=int)
    id           = request.args.get('id'  ,         default="", type=str)
    search_store = request.args.get('search_store', default="", type=str)
    choice_type  = request.args.get('choice_type',  default="", type=str)

    if search_store:
        stores = [store for store in stores if search_store in store[1]]
    if choice_type:
        stores = [store for store in stores if choice_type == store[2]]
    if id:
        storedata = [store for store in stores if id == store[0]]
        return render_template("click_storeid.html", headers = headers, 
                               storedata = storedata, storename = stores[0][1],
                               page = page, search_store=search_store)
    
    pagemaker = Pagination()
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(stores, page, data_per_page, page_per_pagination)
    
    return render_template("stores.html", headers=headers, stores=stores[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_store=search_store, choice_type=choice_type)

if __name__  == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)