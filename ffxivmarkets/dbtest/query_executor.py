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
