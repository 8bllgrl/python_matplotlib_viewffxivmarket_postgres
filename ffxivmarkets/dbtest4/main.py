import matplotlib.pyplot as plt
from db_connector import connect_to_database, fetch_sales_data
from data_processor import calculate_daily_profits, plot_profit_graph, plot_profit_barchart


def main():
    # Connect to the database
    conn = connect_to_database()

    # Fetch sales data
    sales_data = fetch_sales_data(conn)

    # Close the database connection
    conn.close()

    # Selected item IDs
    selected_item_ids = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]  # Example: Replace with your desired item IDs

    # Calculate daily profits and item names for selected item IDs
    selected_sales_data = [sale for sale in sales_data if sale[0] in selected_item_ids]
    daily_profits, item_names = calculate_daily_profits(selected_sales_data)

    # Plot profit graph

    # plot_profit_graph(daily_profits, item_names)
    plot_profit_barchart(daily_profits, item_names)


if __name__ == "__main__":
    main()
