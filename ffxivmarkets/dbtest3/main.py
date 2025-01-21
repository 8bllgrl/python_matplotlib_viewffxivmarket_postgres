import matplotlib.pyplot as plt
from db_connector import connect_to_database, fetch_sales_data
from data_processor import calculate_daily_profits, plot_profit_graph


def main():
    # Connect to the database
    conn = connect_to_database()

    # Fetch sales data
    sales_data = fetch_sales_data(conn)

    # Close the database connection
    conn.close()

    # Calculate daily profits and item names
    daily_profits, item_names = calculate_daily_profits(sales_data)

    # Plot profit graph
    plot_profit_graph(daily_profits, item_names)


if __name__ == "__main__":
    main()
