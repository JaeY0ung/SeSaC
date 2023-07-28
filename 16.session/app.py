from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "abcd1234"

items = {
    'item1': {'name': '장난감', 'price': 1000},
    'item2': {'name': '과자', 'price': 2000},
    'item3': {'name': '물', 'price': 3000}
}

@app.route('/')
def index():
    return render_template("index.html", items=items)


@app.route('/add_to_cart/<item_code>')
def add_to_cart(item_code):
    if 'cart' not in session:
        session['cart'] = {}

    # 카트에 물건 담기
    for item_id, item_info in items.items():
        if item_id == item_code:
            price = item_info['price'] 
            break
    print(session['cart'])

    if item_code in session['cart']:
        session["cart"][item_code]['count'] += 1
        session["cart"][item_code]['sum'] += price
    else:
        session["cart"][item_code] = {'count':1, 'sum': price}
    session["cart"][item_code]['name'] = items[item_id]['name']
    

    session.modified = True
    print(session['cart'])
    # 담은 이름 확인
    return redirect(url_for('index'))

@app.route('/view_cart')
def view_cart():
    print([i['sum'] for i in session['cart'].values()])
    session['total'] = sum([i['sum'] for i in session['cart'].values()])
    total = 0
    if "total" in session:
        total = session['total']

    cart = session["cart"]
    return render_template("cart.html", cart=cart, items=items, total=total)


@app.route('/remove_item_from_cart/<item_code>')
def remove_item_from_cart(item_code):
    session['cart'].pop(item_code)

    # 세션 데이터가 수정되었음을 Flask-> Client 브라우저에게 알림
    session.modified = True

    return redirect(url_for('view_cart'))


if __name__ == '__main__':
    app.run(debug=True, port=8090)