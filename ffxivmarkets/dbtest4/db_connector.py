import os
import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        dbname=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT')
    )
    return conn

def fetch_sales_data_nameless(conn):

    cursor = conn.cursor()
    cursor.execute("SELECT itemid, saletimestamp::date AS sale_date, priceperunit, quantity FROM ffxiv_sales")
    sales_data = cursor.fetchall()
    cursor.close()
    return sales_data

def fetch_sales_data(conn):

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