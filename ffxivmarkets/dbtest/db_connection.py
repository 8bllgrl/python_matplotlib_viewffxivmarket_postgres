# db_connection.py
import psycopg2


def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="ffxivmarkets",
            user="postgres",
            password="Mew_&_Kuromi.",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None
