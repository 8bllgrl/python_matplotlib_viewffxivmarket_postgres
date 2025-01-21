# db_connection.py
import os

import psycopg2


def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT')
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None
