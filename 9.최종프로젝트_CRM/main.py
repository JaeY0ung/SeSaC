from flask import Flask
from home.views import home_bp
from login.veiws import login_bp
from user.views import user_bp
from order.views import order_bp
from orderitem.views import orderitem_bp
from item.views import item_bp
from store.views import store_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
app.register_blueprint(orderitem_bp)
app.register_blueprint(item_bp)
app.register_blueprint(store_bp)



if __name__  == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)