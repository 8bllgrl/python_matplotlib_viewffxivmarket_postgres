import matplotlib.pyplot as plt
from db_connector import connect_to_database, fetch_sales_data, fetch_highest_lowest_prices, \
    fetch_sales_data_avg_price_by_item
from data_processor import calculate_daily_profits, plot_profit_graph_with_7_day_averages, \
    plot_highest_lowest_prices_barchart, plot_profit_graph_avgs, calculate_daily_profits_avg_ppu


def main():
    # Connect to the database
    conn = connect_to_database()

    sales_data = fetch_sales_data_avg_price_by_item(conn)
    conn.close()
    daily_profits, item_names = calculate_daily_profits_avg_ppu(sales_data)
    plot_profit_graph_avgs(daily_profits,item_names)

if __name__ == "__main__":
    main()
