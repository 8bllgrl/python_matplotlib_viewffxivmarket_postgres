# query_execution.py
import psycopg2

def execute_query(conn, query):
    try:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows
    except psycopg2.Error as e:
        print("Error executing query:", e)
        return None

def get_sales_with_item_names(conn):
    query = """
    SELECT s.saletimestamp, s.priceperunit, s.quantity, i.itemname 
    FROM ffxiv_sales s
    JOIN itemnames i ON s.itemid = i.itemid
    """
    return execute_query(conn, query)
