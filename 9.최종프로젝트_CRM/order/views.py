from flask import Blueprint, request,render_template
from File import File
from Pagination import Pagination
import sqlite3

order_bp = Blueprint('order', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@order_bp.route('/orders')
def orders_info():

    page         = request.args.get('page',         default=1,  type=int)
    click_id     = request.args.get('id'  ,         default="", type=str)
    search       = request.args.get('search',       default="", type=str)
    choice_year  = request.args.get('choice_year',  default="", type=str)
    choice_month = request.args.get('choice_month', default="", type=str)
    choice_day   = request.args.get('choice_day',   default="", type=str)
    
    query = '''SELECT Id, OrderAt, StoreId, UserId 
               FROM orders
               WHERE 1=1   
            '''
    #? search 는 Order Id 로 찾음
    if search:
        query += f" AND Id LIKE '%{search}%'"
    if choice_year:
        query += f" AND SUBSTR(OrderAt, 1, 4) = '{choice_year}'"
    if choice_month:
        query += f" AND SUBSTR(OrderAt, 6, 2) = '{choice_month}'"
    if choice_day:
        query += f" AND SUBSTR(OrderAt, 9, 2) = '{choice_day}'"
    if click_id:
        query += f" AND Id = '{click_id}'"

    cursor.execute(query)
    #? 헤더
    headers = [data[0] for data in cursor.description]
    orders = cursor.fetchall()

    if click_id:
        return render_template("order_detail.html", headers = headers, 
                               data = orders[0], page = page, search=search)
    
    pagemaker = Pagination()
    pagemaker.makepagination(orders, page)
    
    return render_template("order.html",
                           headers = headers, datas = orders[pagemaker.start_index : pagemaker.end_index + 1], 
                           page = page, total_page = pagemaker.total_page, 
                           pagination_start = pagemaker.pagination_start, pagination_end = pagemaker.pagination_end, 
                           move_page_front = pagemaker.move_page_front, move_page_back = pagemaker.move_page_back,
                           search = search,
                           choice_year = choice_year, choice_month = choice_month, choice_day = choice_day)