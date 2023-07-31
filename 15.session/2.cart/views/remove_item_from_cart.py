from flask import Blueprint, Flask, render_template, redirect, url_for, session

bp = Blueprint('remove_item_from_car', __name__, url_prefix='/remove_item_from_cart')

#? 장바구니에서 물건 제거
@bp.route('/<cart_item_code>')
def remove_item_from_cart(cart_item_code):
    session['cart'].pop(cart_item_code)

    #? 세션 데이터가 수정되었음을 Flask-> Client 브라우저에게 알림
    session.modified = True
    
    print("장바구니 물건 제거")

    return redirect(url_for('view_cart'))
    
