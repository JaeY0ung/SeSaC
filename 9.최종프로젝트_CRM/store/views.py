from flask import Blueprint, request,render_template
from File import File
from Pagination import Pagination
import sqlite3

store_bp = Blueprint('store', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@store_bp.route('/stores')
def stores_info():
    headers = ['Id', 'Name', 'Type', 'Address']
    query = "SELECT Id, Name, Type, Address FROM 'stores'"
    cursor.execute(query)
    stores = cursor.fetchall()
    print(stores)

    page         = request.args.get('page',         default=1,  type=int)
    id           = request.args.get('id'  ,         default="", type=str)
    search_store = request.args.get('search_store', default="", type=str)
    choice_type  = request.args.get('choice_type',  default="", type=str)

    if search_store:
        stores = [store for store in stores if search_store in store[1]]
    if choice_type:
        stores = [store for store in stores if choice_type in store[2]]
    if id:
        storedata = [store for store in stores if id == store[0]]
      
        cursor.execute("""SELECT strftime('%Y-%m', orders.OrderAt) AS month, 
                        SUM('items'.'UnitPrice') AS Revenue
                        FROM 'orders'
                        JOIN 'orderitems' ON orders.Id = orderitems.Orderid
                        JOIN 'items' ON orderitems.ItemId = items.id
                        WHERE orders.StoreId = ?
                        GROUP BY strftime('%Y-%m', orders.OrderAt)
                        """,(id,))
        monthly_revenue = cursor.fetchall()

        labels = []
        revenues = []

        for row in monthly_revenue:
            labels.append(row[0])
            revenues.append(row[1])

        return render_template("click_storeid.html", headers = headers, 
                               storedata = storedata, storename = stores[0][1],
                               page = page, search_store=search_store,
                               monthly_revenue=monthly_revenue, labels=labels, revenues=revenues)
    
    cursor.execute("""SELECT strftime('%Y-%m', orders.OrderAt) AS month, 
                        SUM('items'.'UnitPrice') AS Revenue
                        FROM 'orders'
                        JOIN 'orderitems' ON orders.Id = orderitems.Orderid
                        JOIN 'items' ON orderitems.ItemId = items.id
                        GROUP BY strftime('%Y-%m', orders.OrderAt)
                        """)
    monthly_revenue = cursor.fetchall()
    labels = []
    revenues = []
    for row in monthly_revenue:
        labels.append(row[0])
        revenues.append(row[1])

    pagemaker = Pagination()
    pagemaker.makepagination(stores, page)

    start_index = pagemaker.start_index
    end_index = pagemaker.end_index
    total_page = pagemaker.total_page
    pagination_start = pagemaker.pagination_start
    pagination_end = pagemaker.pagination_end
    move_page_front = pagemaker.move_page_front
    move_page_back = pagemaker.move_page_back

    return render_template("stores.html", headers=headers, stores=stores[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end,
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_store=search_store, choice_type=choice_type,
                           monthly_revenue=monthly_revenue, labels=labels, revenues=revenues)