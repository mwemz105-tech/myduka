import psycopg2 

# establishing a new connection to a postgres db
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='BANNERLORD254',dbname='myduka')

# cur object for db operations
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    print(products_data)

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
