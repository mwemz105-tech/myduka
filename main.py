from flask import Flask, render_template, request, redirect, url_for
from database import get_products,insert_products
from database import get_sales,insert_sales
from database import get_stocks, insert_stock

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

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print("Product added successfully")
    return redirect(url_for('products'))


#sales route
@app.route('/sales')
def sales():
    sales_data = get_sales()
    return render_template('sales.html', sales_data=sales_data)

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        selling_price = request.form['selling_price']

        new_sale = (product_id,quantity,selling_price)
        insert_sales(new_sale)
        print("Sale recorded successfully")
    return redirect(url_for('sales'))


#stocks route
@app.route('/stocks')
def stocks():
    stocks_data=get_stocks()
    return render_template('stocks.html',stocks_data=stocks_data)

@app.route('/add_stocks',methods=['GET','POST'])
def add_stocks():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']

        new_stock = (product_id, quantity)
        insert_stock(new_stock)
        print("Stock added successfully")
    return redirect(url_for('stocks'))



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

