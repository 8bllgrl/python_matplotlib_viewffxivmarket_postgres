from ffxivmarkets.main.db.data_processor import calculate_daily_profits, plot_profit_graph
from ffxivmarkets.main.db.db_connector import connect_to_database, fetch_sales_data

def mainGraph():
    conn = connect_to_database()
    sales_data = fetch_sales_data(conn)
    conn.close()
    daily_profits, item_names = calculate_daily_profits(sales_data)
    plot_profit_graph(daily_profits, item_names)
