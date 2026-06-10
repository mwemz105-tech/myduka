from flask import Flask, render_template

#Flask Instance
app = Flask(__name__)

#index route
@app.route('/')
def home():
    return render_template("index.html")


#products route
@app.route("/products")
def products():
    return render_template('products.html')


#sales route
@app.route('/sales')
def sales():
    return render_template('sales.html')




#run your application
app.run()

