from flask import Blueprint, request,render_template
from File import File
from Pagination import Pagination
import sqlite3

store_bp = Blueprint('store', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@store_bp.route('/stores')
def stores_info():
    page         = request.args.get('page',        default= 1, type=int)
    click_id     = request.args.get('id'  ,        default="", type=str)
    search       = request.args.get('search',      default="", type=str)
    choice_type  = request.args.get('choice_type', default="", type=str)

    query = '''SELECT Id, Name, Type, Address 
               FROM 'stores'
               WHERE 1=1
            '''
    if search:
        query += f" AND Name LIKE '%{search}%'"
    if choice_type:
        query += f" AND Type = '{choice_type}'"
    if click_id:
        query += f" AND Id = '{click_id}'"

    cursor.execute(query)
    headers = [data[0] for data in cursor.description]
    stores = cursor.fetchall()

    #? 통계를 위한 query2 Default 
    query2 = '''SELECT strftime('%Y-%m', orders.OrderAt) AS month, 
                       SUM('items'.'UnitPrice') AS Revenue,
                       COUNT('items') AS ItemCount
                FROM 'orders'
                JOIN 'orderitems' ON orders.Id = orderitems.Orderid
                JOIN 'items' ON orderitems.ItemId = items.id
             '''
    if click_id:
        #? store(가게)의 월 별 수입 통계를 보여주기 위함
        query2 += f"WHERE orders.StoreId = '{click_id}'"

    query2 += "GROUP BY strftime('%Y-%m', orders.OrderAt)"

    cursor.execute(query2)
    monthly_revenue = cursor.fetchall()

    # Chart.js 를 위한 인자
    labels = [row[0] for row in monthly_revenue]
    revenues = [row[1] for row in monthly_revenue]
    itemCount = [row[2] for row in monthly_revenue]
    
    if click_id:
        return render_template("click_storeid.html", headers = headers, 
                               storedata = stores[0], page = page, search=search,
                               monthly_revenue = monthly_revenue, labels = labels, 
                               revenues = revenues, itemCount = itemCount)
    
    pagemaker = Pagination()
    pagemaker.makepagination(stores, page)
    fileReader = File()
    storetype_list = [row[0] for row in fileReader.read('../8.CRM_Generator/src/store_types.txt')]

    return render_template("stores.html", headers = headers, stores = stores[pagemaker.start_index : pagemaker.end_index + 1], 
                           page=page, total_page = pagemaker.total_page, storetype_list = storetype_list,
                           pagination_start = pagemaker.pagination_start, pagination_end = pagemaker.pagination_end,
                           move_page_front = pagemaker.move_page_front, move_page_back = pagemaker.move_page_back,
                           search = search, choice_type=choice_type,
                           monthly_revenue = monthly_revenue, labels = labels, revenues = revenues)