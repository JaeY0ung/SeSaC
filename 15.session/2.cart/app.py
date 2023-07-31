from flask import Flask, render_template, session, redirect, url_for
import utils
from views import remove_item_from_cart

app = Flask(__name__)
app.secret_key = utils.SECRET_KEY
app.register_blueprint(remove_item_from_cart.bp)

items = utils.items

@app.route('/')
def index():
    return render_template("index.html", items = items)

#? 클릭하여 장바구니에 추가
@app.route('/add_to_cart/<cart_item_code>')
def add_to_cart(cart_item_code):
    if 'cart' not in session:
        session['cart'] = dict()

    # 장바구니에 담기 클릭한 물건의 가격을 price에 저장
    for item_code, item_info in items.items():
        if item_code == cart_item_code:
            price = item_info['price'] 
            break

    if cart_item_code in session['cart']:
        session["cart"][cart_item_code]['count'] += 1
        session["cart"][cart_item_code]['sum'] += price
    else:
        session["cart"][cart_item_code] = {'count': 1, 'sum': price}
    

    #? 카트에 물건 이름 가져오기
    session["cart"][cart_item_code]['name'] = items[cart_item_code]['name']

    session.modified = True
    print("장바구니에 추가")

    return redirect(url_for('index'))

#? 장바구니 창
@app.route('/view_cart')
def view_cart():
    print("장바구니 창 열림")
    print([i['sum'] for i in session['cart'].values()])
    session['total'] = sum([i['sum'] for i in session['cart'].values()])
    total = 0
    if "total" in session:
        total = session['total']

    cart = session["cart"]
    return render_template("cart.html", cart=cart, items=items, total=total)

# #? 장바구니에서 물건 제거
# @app.route('/remove_item_from_cart/<cart_item_code>')
# def remove_item_from_cart(cart_item_code):
#     session['cart'].pop(cart_item_code)

#     #? 세션 데이터가 수정되었음을 Flask-> Client 브라우저에게 알림
#     session.modified = True
    
#     print("장바구니 물건 제거")

#     return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True, port=8090)