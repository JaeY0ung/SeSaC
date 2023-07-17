from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination
import sqlite3

orderitem_bp = Blueprint('orderitem', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@orderitem_bp.route('/orderitems')
def orderitems_info():
    page     = request.args.get('page',   default= 1, type=int)
    click_id = request.args.get('id'  ,   default="", type=str)
    search   = request.args.get('search', default="", type=str)

    query = '''SELECT Id, OrderId, ItemId 
               FROM 'orderitems'
               WHERE 1=1
            '''
    if search:
        query += f" AND Id LIKE '%{search}%'"
    if click_id:
        query += f" AND Id = '{click_id}'"

    cursor.execute(query)
    #? 헤더
    headers = [ data[0] for data in cursor.description]
    orderitems = cursor.fetchall()

    if click_id:
        return render_template("click_orderitemid.html", headers = headers, 
                               orderitemdata = orderitems[0],
                               page = page, search = search)
    
    pagemaker = Pagination()
    pagemaker.makepagination(orderitems, page)

    return render_template("orderitems.html",
                           headers = headers, orderitems = orderitems[pagemaker.start_index : pagemaker.end_index + 1], 
                           page = page, total_page = pagemaker.total_page, 
                           pagination_start = pagemaker.pagination_start, pagination_end = pagemaker.pagination_end,
                           move_page_front = pagemaker.move_page_front, move_page_back = pagemaker.move_page_back,
                           search = search)