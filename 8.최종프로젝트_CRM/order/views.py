from flask import Blueprint, request,render_template
from File import File
from Pagination import Pagination

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders')
def orders_info():
    file_rdr = File()
    data     = file_rdr.read("./csv/crm_order.csv")
    headers  = [header.strip() for header in data[0]]
    orders   = data[1:]

    page         = request.args.get('page',         default=1,  type=int)
    id           = request.args.get('id'  ,         default="", type=str)
    search_order = request.args.get('search_order', default="", type=str)
    # choice_date  = request.args.get('choice_date',  default="", type=str)

    choice_year  = request.args.get('choice_year',  default="", type=str)
    choice_month = request.args.get('choice_month',  default="", type=str)
    choice_day   = request.args.get('choice_day',  default="", type=str)
    
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
    pagemaker.makepagination(orders, page)

    start_index = pagemaker.start_index
    end_index = pagemaker.end_index
    total_page = pagemaker.total_page
    pagination_start = pagemaker.pagination_start
    pagination_end = pagemaker.pagination_end
    move_page_front = pagemaker.move_page_front
    move_page_back = pagemaker.move_page_back
    
    return render_template("orders.html",
                           headers=headers, orders=orders[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end, 
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_order=search_order,
                           choice_year=choice_year, choice_month=choice_month, choice_day=choice_day)