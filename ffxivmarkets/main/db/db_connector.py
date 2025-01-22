#db_connector.py
from datetime import datetime, timedelta
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


def fetch_sales_data_w_days(conn, days_ago):
    start_date = datetime.now() - timedelta(days=days_ago)

    cursor = conn.cursor()
    cursor.execute("""
        SELECT ffsales.itemid, inames.itemname, ffsales.saletimestamp::date AS sale_date,
               ffsales.priceperunit, ffsales.quantity 
        FROM ffxiv_sales AS ffsales 
        JOIN itemnames AS inames ON ffsales.itemid = inames.itemid
        WHERE ffsales.saletimestamp::date >= %s
    """, (start_date,))

    sales_data = cursor.fetchall()
    cursor.close()
    return sales_data
def fetch_highest_lowest_prices(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT itemid, MAX(priceperunit) AS highest_price, MIN(priceperunit) AS lowest_price 
        FROM ffxiv_sales 
        GROUP BY itemid
    """)
    prices_data = cursor.fetchall()
    cursor.close()
    return prices_data

def fetch_sales_data_avg_price_by_item(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            DATE(saletimestamp) AS sale_date,
            fs.itemid,
            i.itemname,
            AVG(fs.priceperunit) AS average_price_per_unit
        FROM 
            ffxiv_sales fs
        INNER JOIN 
            ItemNames i ON fs.itemid = i.itemid
        GROUP BY 
            DATE(fs.saletimestamp),
            fs.itemid,
            i.itemname
        ORDER BY 
            sale_date,
            fs.itemid;
    """)
    sales_data = cursor.fetchall()
    cursor.close()
    return sales_data
