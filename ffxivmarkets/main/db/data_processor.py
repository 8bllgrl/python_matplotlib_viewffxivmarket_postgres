import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import mplcursors
from matplotlib.colors import Normalize
from matplotlib.dates import DateFormatter
from matplotlib.ticker import FuncFormatter



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
    all_profits = [profit for profits in daily_profits.values() for profit in profits.values()]  # Flatten profits
    min_profit = min(all_profits)
    max_profit = max(all_profits)

    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]

        line, = plt.plot(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})', alpha=0.3)  # Grey out lines
        line.set_gid(str(item_id))

    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of Each Day for Each Item')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))  # Date format with only month and day
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

    # plt.ylim(min_profit, max_profit)  # Set y-axis limits based on the range of profit values

    plt.ylim(min_profit * 0.9, max_profit * 1.1)  # Adjusted scale to give some buffer space

    formatter = FuncFormatter(lambda x, _: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        item_id = int(sel.artist.get_gid())  # Get the item ID from the line's GID
        sel.annotation.set_text(sel.artist.get_label())
        sel.annotation.set_visible(True)
        for line in plt.gca().lines:
            if int(line.get_gid()) == item_id:
                line.set_alpha(1)
            else:
                line.set_alpha(0.3)  # Grey out other lines
        plt.draw()

    # plt.legend()
    plt.show()
def calculate_7_day_averages(daily_profits):
    seven_day_averages = {}
    for item_id, profits in daily_profits.items():
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]
        seven_day_avg = np.convolve(profits_per_day, np.ones(7) / 7, mode='valid')
        seven_day_averages[item_id] = seven_day_avg
    return seven_day_averages
def plot_profit_graph_with_7_day_averages(daily_profits, item_names):
    seven_day_averages = calculate_7_day_averages(daily_profits)

    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]  # Retrieve item name
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]

        line, = plt.plot(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})', alpha=0.3)  # Grey out lines
        line.set_gid(str(item_id))  # Set a unique ID for each line

        # Plot 7-day moving average
        if item_id in seven_day_averages:
            avg_dates = dates[6:]  # Adjust dates for 7-day moving average
            avg_profits = seven_day_averages[item_id]
            if len(avg_dates) >= 7:  # Ensure at least 7 dates are available
                plt.plot(avg_dates, avg_profits, linestyle='--', color=line.get_color(), alpha=0.8)

    plt.xlabel('Date')
    plt.ylabel('Total Profit')
    plt.title('Total Profit of Each Day for Each Item with 7-Day Moving Averages')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))  # Date format with only month and day
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

    # Add annotations for item names on hover
    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_hover(sel):
        item_id = int(sel.artist.get_gid())
        item_name = sel.artist.get_label().split(' (Item ID')[0]
        sel.annotation.set_text(item_name)
        sel.annotation.set_visible(True)
        for line in plt.gca().lines:
            if int(line.get_gid()) == item_id:
                line.set_alpha(1)
            else:
                line.set_alpha(0.3)
        plt.draw()

    #plt.legend()
    plt.show()
def plot_profit_barchart(daily_profits, item_names):
    total_profits = []
    item_ids = []

    # Calculate total profit for each item
    for item_id, profits in daily_profits.items():
        total_profit = sum(profits.values())
        total_profits.append(total_profit)
        item_ids.append(item_id)

    # Sort items based on total profit
    sorted_indices = np.argsort(total_profits)
    total_profits_sorted = [total_profits[i] for i in sorted_indices]
    item_ids_sorted = [item_ids[i] for i in sorted_indices]
    item_names_sorted = [item_names[item_id] for item_id in item_ids_sorted]

    norm = Normalize(vmin=min(total_profits_sorted), vmax=max(total_profits_sorted))

    # Aesthetically pleasing colors
    cmap = plt.cm.coolwarm

    fig, ax = plt.subplots()

    bars = ax.bar(item_names_sorted, total_profits_sorted, color=cmap(norm(total_profits_sorted)))

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Total Profit')

    formatter = FuncFormatter(lambda x, _: f'{int(x):,}')
    cbar.ax.yaxis.set_major_formatter(formatter)

    ax.set_xlabel('Item')
    ax.set_ylabel('Total Profit')
    ax.set_title('Total Profit for Each Item')

    plt.xticks(rotation=45)

    for bar, v in zip(bars, total_profits_sorted):
        ax.text(bar.get_x() + bar.get_width() / 2, v, f' ${int(v):,}', ha='center', va='bottom')

    plt.show()
def plot_highest_lowest_prices_barchart(highest_prices, lowest_prices, item_names):
    highest_prices_list = []
    lowest_prices_list = []
    item_ids = []

    for item_id in highest_prices.keys():
        highest_prices_list.append(highest_prices[item_id])
        lowest_prices_list.append(lowest_prices[item_id])
        item_ids.append(item_id)

    sorted_indices = sorted(range(len(lowest_prices_list)), key=lambda k: lowest_prices_list[k])
    highest_prices_sorted = [highest_prices_list[i] for i in sorted_indices]
    lowest_prices_sorted = [lowest_prices_list[i] for i in sorted_indices]
    item_ids_sorted = [item_ids[i] for i in sorted_indices]
    item_names_sorted = [item_names[item_id] for item_id in item_ids_sorted]

    fig, ax = plt.subplots()

    # Define bar width
    bar_width = 0.35

    index = np.arange(len(item_ids_sorted))

    # Plot bars for highest prices
    bars1 = ax.bar(index, highest_prices_sorted, bar_width, label='Highest Price')
    # Plot bars for lowest prices
    bars2 = ax.bar(index + bar_width, lowest_prices_sorted, bar_width, label='Lowest Price')

    ax.set_xlabel('Item')
    ax.set_ylabel('Price')
    ax.set_title('All-Time Highest and Lowest Prices for Each Item')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(item_names_sorted)
    plt.xticks(rotation=45)

    ax.legend()

    def autolabel(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'${height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    autolabel(bars1)
    autolabel(bars2)

    plt.tight_layout()
    plt.show()

def plot_profit_graph_avgs(daily_profits, item_names):
    for item_id, profits in daily_profits.items():
        item_name = item_names[item_id]
        dates = sorted(profits.keys())
        profits_per_day = [profits[date] for date in dates]

        plt.plot(dates, profits_per_day, label=f'{item_name} (Item ID: {item_id})', alpha=0.7)

    plt.xlabel('Date')
    plt.ylabel('Average Price per Unit')
    plt.title('Average Price per Unit for Each Day for Each Item')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d'))
    plt.xticks(rotation=45)


    plt.show()

def calculate_daily_profits_avg_ppu(sales_data):
    daily_profits = defaultdict(lambda: defaultdict(float))
    item_names = {}
    for sale_date, item_id, item_name, avg_price_per_unit in sales_data:
        daily_profits[item_id][sale_date] = avg_price_per_unit
        if item_id not in item_names:
            item_names[item_id] = item_name
    return daily_profits, item_names