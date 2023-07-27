from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.instance_path = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user-sample.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

class User(db.Model):
    #? 테이블 이름 정의 (옵션)
    __tablename__ = 'users'

    #? 컬럼 셋업
    id        = db.Column(db.String(64), primary_key = True)
    name      = db.Column(db.String(16))
    gender    = db.Column(db.String(64))
    age       = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address   = db.Column(db.String(64))

    #? 관계 (relation) 셋업
    orderR = db.relationship('Order', backref='users')

    def __repr__(self):
        return f'<User {self.name}, {self.gender}, {self.age}, {self.birthdate}, {self.address}'
    
class Store(db.Model):
    #? 테이블 이름 정의 (옵션)
    __tablename__ = 'stores'
    #? 컬럼 셋업
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))

    storeR = db.relationship('Order', backref='stores')
    def __repr__(self):
        return f'<Store {self.name}, {self.type}, {self.address}'
    
class Order(db.Model):
    #? 테이블 이름 정의 (옵션)
    __tablename__ = 'orders'
    #? 컬럼 셋업
    id      = db.Column(db.String(64), primary_key=True)
    orderat = db.Column(db.String(32))
    storeid = db.Column(db.String(64), db.ForeignKey('stores.id'))
    userid  = db.Column(db.String(64), db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Order {self.id}, {self.orderat}'

@app.route('/')
def home():
    # users = User.query.all()
    # stores = Store.query.all()
    # print(users)
    # for store in stores:
    #     print(store)

    # users = User.query.filter_by(name='윤수빈').first()
    # print(users)
    # order_by_user = users.orderR
    # print(order_by_user)

    #? 쿼리문을 작성하시오
    shop_by_user = db.session.query(User, Order, Store)\
                             .join(Order, User.id == Order.userid)\
                             .join(Store, Store.id == Order.storeid)\
                             .filter(User.name == '윤수빈').first()
    print(shop_by_user)

    #? 쿼리문을 relation , backref 이용
    users = User.query.filter_by(name="윤수빈").first()
    order_by_user = users.orderR

    #? 윤수빈이 주문한 주문내역
    for order in order_by_user:
        store = order.stores
        print(f"윤수빈이 방문한 상점은 {store.name} 시간은 {order.orderat}")

    return 'Hello'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()