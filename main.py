from flask import Flask, render_template
from database import get_products
from database import get_sales
from database import get_stocks

#Flask Instance
app = Flask(__name__)

#index route
@app.route('/')
def home():
    return render_template("index.html")


#products route
@app.route("/products")
def products():
    products_data = get_products()
    return render_template('products.html',products_data=products_data)


#sales route
@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html', sales_data=sales_data)


#stocks route
@app.route('/stocks')
def stocks():
    stocks_data=get_stocks()
    return render_template('stocks.html',stocks_data=stocks_data)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


#run your application
app.run()

