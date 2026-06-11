import psycopg2 

# establishing a new connection to a postgres db
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='BANNERLORD254',dbname='myduka')

# cur object for db operations
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def insert_products(values):
    cur.execute(f"insert into products(name, buying_price, selling_price)values{values}")
    conn.commit()

product1=('samsung phone',30000,40000)
product2=('LG TV',50000,60000)

insert_products(product1)
insert_products(product2)

x=5
y=10
z=x+y

def get_sum(x,y):
    return x+y

def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",(values))
    conn.commit()

    product3=('book',1200,1800)
    insert_products2(product3)

# task1
def get_stocks():
    cur.execute("select * from stock")
    stocks_data = cur.fetchall()
    return stocks_data

stocks_data = get_stocks()
print(stocks_data)

# task2

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

sales1=(1,5)
sales2=(2,7)
sales3=(3,23)





sales_data=get_sales()
print(sales_data)

# task3
def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",values)
    conn.commit()

stock1=(1,27)
stock2=(2,35)
stock3=(3,56)

# insert_stock(stock1)
# insert_stock(stock2)
# insert_stock(stock3)

stocks_data = get_stocks()
print(stocks_data)

def sales_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, SUM(sales.quantity * products.selling_price) 
        AS sales_per_day FROM sales JOIN products ON sales.pid = products.id 
        GROUP BY DATE(created_at) ORDER BY sale_date; 

""")
    daily_sales=cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
        SELECT DATE(sales.created_at) AS sale_date, 
        SUM((products.selling_price - products.buying_price) * sales.quantity) 
        AS profit_per_day FROM sales JOIN products ON sales.pid = products.id 
        GROUP BY DATE(created_at) ORDER BY sale_date;
""")
    daily_profit=cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        SELECT name, SUM(sales.quantity) AS sales_per_product FROM sales
        JOIN products ON sales.pid = products.id GROUP BY name;
""")
    product_sales=cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
        SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) 
        AS profit_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
""")
    product_profit=cur.fetchall()
    return product_profit

# 1. Student

# identity → Student
# state → name, student_id, grade_level
# behaviour → study, take_exam, attend_class

# 2. Car

# identity → Car
# state → make, model, year
# behaviour → drives, brakes, honks