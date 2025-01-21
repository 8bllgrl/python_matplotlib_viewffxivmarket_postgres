import matplotlib.pyplot as plt
from collections import defaultdict

import mplcursors
import numpy as np
from matplotlib import ticker
from matplotlib.dates import DateFormatter

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
    all_profits = []

    for profits in daily_profits.values():
        all_profits.extend(profits.values())

    min_profit = min(all_profits)
    max_profit = max(all_profits)
    y_padding = 0.1 * (max_profit - min_profit)
    y_min = min_profit - y_padding
    y_max = max_profit + y_padding

    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]

        line, = plt.plot(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})', alpha=0.3)
        line.set_gid(str(item_id))

    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of Each Day for Each Item')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))
    plt.xticks(rotation=45)

    plt.ylim(y_min, y_max)

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        item_id = int(sel.artist.get_gid())
        sel.annotation.set_text(sel.artist.get_label())
        sel.annotation.set_visible(True)
        for line in plt.gca().lines:
            if int(line.get_gid()) == item_id:
                line.set_alpha(1)
            else:
                line.set_alpha(0.3)
        plt.draw()

    plt.show()

def plot_profit_barchart(daily_profits, item_names):

    total_profits = []
    item_ids = []

    for item_id, profits in daily_profits.items():
        total_profit = sum(profits.values())
        total_profits.append(total_profit)
        item_ids.append(item_id)

    sorted_indices = np.argsort(total_profits)
    total_profits_sorted = [total_profits[i] for i in sorted_indices]
    item_ids_sorted = [item_ids[i] for i in sorted_indices]
    item_names_sorted = [item_names[item_id] for item_id in item_ids_sorted]

    plt.barh(item_names_sorted, total_profits_sorted, color='skyblue')
    plt.xlabel('Total Profit')
    plt.ylabel('Item')
    plt.title('Total Profit for Each Item')

    for i, v in enumerate(total_profits_sorted):
        plt.text(v, i, f' ${v:,.2f}', ha='left', va='center')

    plt.show()

def plot_profit_graph_bar(daily_profits, item_names):
    dates = sorted(next(iter(daily_profits.values())).keys())

    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]
        profits_per_day = [profits[date] for date in dates]

        plt.bar(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})', alpha=0.3)

    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of Each Day for Each Item')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))
    plt.xticks(rotation=45)

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        sel.annotation.set_visible(True)
        sel.annotation.set_text(sel.artist.get_label())
        plt.draw()

    plt.show()