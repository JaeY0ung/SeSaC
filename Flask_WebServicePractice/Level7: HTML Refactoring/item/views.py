from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination

item_bp = Blueprint('item', __name__)

@item_bp.route('/items')
def items_info():
    file_rdr = File()
    data     = file_rdr.read("src/item.csv")
    headers  = [header.strip() for header in data[0]]
    items    = data[1:]

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
    pagemaker.makepagination(items, page)

    start_index = pagemaker.start_index
    end_index = pagemaker.end_index
    total_page = pagemaker.total_page
    pagination_start = pagemaker.pagination_start
    pagination_end = pagemaker.pagination_end
    move_page_front = pagemaker.move_page_back
    move_page_back = pagemaker.move_page_back
    
    return render_template("items.html",
                           headers=headers, items=items[start_index : end_index + 1], 
                           page=page, total_page=total_page, 
                           pagination_start=pagination_start, pagination_end=pagination_end, 
                           move_page_front=move_page_front, move_page_back=move_page_back,
                           search_item=search_item, choice_type=choice_type)