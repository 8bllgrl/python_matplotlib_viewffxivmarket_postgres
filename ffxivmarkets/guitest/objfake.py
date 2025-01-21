import matplotlib.pyplot as plt
import numpy as np

class ProfitPoint:
    def __init__(self, day, profit):
        self.day = day
        self.profit = profit

class MonthlyProfit:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, dataset, color='blue'):
        self.datasets.append((dataset, color))

    def plot_profit_graph(self):
        plt.figure(figsize=(12, 6))

        for dataset, color in self.datasets:
            days = [point.day for point in dataset]
            profits = [point.profit for point in dataset]

            z = np.polyfit(days, profits, 3)
            f = np.poly1d(z)
            x_new = np.linspace(min(days), max(days), 100)
            y_new = f(x_new)

            plt.scatter(days, profits, color=color, label='Profit', zorder=5)

            plt.plot(x_new, y_new, color=color, linestyle='-', label='Curve Fit', zorder=4)

        # Add gridlines and labels
        plt.grid(True)
        plt.xlabel('Days')
        plt.ylabel('Profit')
        plt.title('Profit of the Month')
        plt.legend()
        plt.show()

monthly_profit_object = MonthlyProfit()

dataset1 = [ProfitPoint(1, 100), ProfitPoint(2, 150), ProfitPoint(3, 200), ProfitPoint(4, 220)]
dataset2 = [ProfitPoint(1, 80), ProfitPoint(2, 130), ProfitPoint(3, 180), ProfitPoint(4, 200)]
dataset3 = [ProfitPoint(1, 120), ProfitPoint(2, 170), ProfitPoint(3, 220), ProfitPoint(4, 240)]
monthly_profit_object.add_dataset(dataset1, color='blue')
monthly_profit_object.add_dataset(dataset2, color='green')
monthly_profit_object.add_dataset(dataset3, color='red')
monthly_profit_object.plot_profit_graph()
