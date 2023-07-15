from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination
import sqlite3

orderitem_bp = Blueprint('orderitem', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@orderitem_bp.route('/orderitems')
def orderitems_info():
    # file_rdr   = File()
    # data       = file_rdr.read("./csv/crm_orderitem.csv")
    # headers    = [header.strip() for header in data[0]]
    # orderitems = data[1:]

    headers = ['Id', 'OrderId', 'ItemId']
    query = "SELECT Id, OrderId, ItemId FROM 'orderitems'"
    cursor.execute(query)
    orderitems = cursor.fetchall()

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
    pagemaker.makepagination(orderitems, page)

    start_index = pagemaker.start_index
    end_index = pagemaker.end_index
    total_page = pagemaker.total_page
    pagination_start = pagemaker.pagination_start
    pagination_end = pagemaker.pagination_end
    move_page_front = pagemaker.move_page_front
    move_page_back = pagemaker.move_page_back

    return render_template("orderitems.html",
                           headers=headers, orderitems=orderitems[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_orderitem=search_orderitem)