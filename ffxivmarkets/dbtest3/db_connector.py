import psycopg2

def connect_to_database():
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="ffxivmarkets",
        user="postgres",
        password="Mew_&_Kuromi.",
        host="localhost",
        port="5432"
    )
    return conn

def fetch_sales_data_nameless(conn):
    # Fetch sales data from the database
    cursor = conn.cursor()
    cursor.execute("SELECT itemid, saletimestamp::date AS sale_date, priceperunit, quantity FROM ffxiv_sales")
    sales_data = cursor.fetchall()
    cursor.close()
    return sales_data

def fetch_sales_data(conn):
    # Fetch sales data along with item names from the database
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ffsales.itemid, inames.itemname, ffsales.saletimestamp::date AS sale_date,
               ffsales.priceperunit, ffsales.quantity 
        FROM ffxiv_sales AS ffsales 
        JOIN itemnames AS inames ON ffsales.itemid = inames.itemid
    """)
    sales_data = cursor.fetchall()
    cursor.close()
    return sales_data