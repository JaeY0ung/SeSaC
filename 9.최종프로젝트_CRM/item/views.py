from flask import Blueprint, request, render_template
from File import File
from Pagination import Pagination
import sqlite3

item_bp = Blueprint('item', __name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@item_bp.route('/items')
def items_info():
    page        = request.args.get('page',        default=1,  type=int)
    click_id    = request.args.get('id'  ,        default="", type=str)
    search      = request.args.get('search',      default="", type=str)
    choice_type = request.args.get('choice_type', default="", type=str)

    query = '''SELECT Id, Name, Type, UnitPrice 
               FROM 'items'
               WHERE 1=1
            '''
    if search:
        query += f" AND NAME LIKE '%{search}%'"
    if choice_type:
        query += f" AND TYPE = '{choice_type}'"
    if click_id:
        query += f" AND Id = '{click_id}'"

    cursor.execute(query)
    headers = [data[0] for data in cursor.description]
    items = cursor.fetchall()

    if click_id:
        return render_template("click_itemid.html", headers = headers, 
                               itemdata = items[0], page = page, search=search)

    pagemaker = Pagination()
    pagemaker.makepagination(items, page)
    
    return render_template("items.html",
                           headers = headers, items = items[pagemaker.start_index : pagemaker.end_index + 1], 
                           page = page, total_page = pagemaker.total_page, 
                           pagination_start = pagemaker.pagination_start, pagination_end = pagemaker.pagination_end, 
                           move_page_front = pagemaker.move_page_front, move_page_back = pagemaker.move_page_back,
                           search = search, choice_type = choice_type)