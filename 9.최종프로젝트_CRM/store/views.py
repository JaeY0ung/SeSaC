from flask import Blueprint, request,render_template
from File import File
from Pagination import Pagination

store_bp = Blueprint('store', __name__)

@store_bp.route('/stores')
def stores_info():
    file_rdr = File()
    data     = file_rdr.read("./csv/crm_store.csv")

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
                           search_store=search_store, choice_type=choice_type)