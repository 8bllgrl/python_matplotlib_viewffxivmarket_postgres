import matplotlib.pyplot as plt
from db_connector import connect_to_database, fetch_sales_data, fetch_highest_lowest_prices
from data_processor import calculate_daily_profits, plot_profit_graph_with_7_day_averages, \
    plot_highest_lowest_prices_barchart


def main():
    # Connect to the database
    conn = connect_to_database()

    # Fetch sales data
    sales_data = fetch_sales_data(conn)

    # Close the database connection

    # Calculate daily profits and item names
    daily_profits, item_names = calculate_daily_profits(sales_data)
    prices_data = fetch_highest_lowest_prices(conn)
    highest_prices = {item_id: highest_price for item_id, highest_price, _ in prices_data}
    lowest_prices = {item_id: lowest_price for item_id, _, lowest_price in prices_data}

    # Plot profit graph with 7-day moving averages
    plot_highest_lowest_prices_barchart(highest_prices, lowest_prices, item_names)

    conn.close()


if __name__ == "__main__":
    main()