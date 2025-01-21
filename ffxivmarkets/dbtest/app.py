from db_connection import connect_to_database
from query_executor import execute_query

def main():
    conn = connect_to_database()
    if conn:
        query = "SELECT * FROM ffxiv_sales"
        rows = execute_query(conn, query)
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data returned from the query.")
        conn.close()
    else:
        print("Connection to the database failed.")

if __name__ == "__main__":
    main()
