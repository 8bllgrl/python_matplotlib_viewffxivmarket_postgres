import matplotlib.pyplot as plt
from collections import defaultdict

def calculate_daily_profits(sales_data):
    daily_profits = defaultdict(lambda: defaultdict(int))
    item_names = {}
    for item_id, item_name, sale_date, price_per_unit, quantity in sales_data:
        profit = price_per_unit * quantity
        daily_profits[item_id][sale_date] += profit
        if item_id not in item_names:
            item_names[item_id] = item_name
    return daily_profits, item_names

def plot_profit_graph(daily_profits, item_names):
    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]
        plt.plot(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})')

    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of Each Day for Each Item')
    plt.legend()
    plt.show()