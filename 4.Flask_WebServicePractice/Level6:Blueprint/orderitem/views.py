from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/orderitems')
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
    start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back = pagemaker.makepagination(orderitems, page)
    
    return render_template("orderitems.html", headers=headers, 
                           orderitems=orderitems[start_index : end_index + 1], page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_orderitem=search_orderitem)