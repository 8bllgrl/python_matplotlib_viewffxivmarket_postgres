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
        # Set the figure size to be wider
        plt.figure(figsize=(12, 6))  # Adjust the width and height as needed

        for dataset, color in self.datasets:
            days = [point.day for point in dataset]
            profits = [point.profit for point in dataset]

            # Fit a curve to the points
            z = np.polyfit(days, profits, 3)
            f = np.poly1d(z)
            x_new = np.linspace(min(days), max(days), 100)
            y_new = f(x_new)

            # Plot the original points
            plt.scatter(days, profits, color=color, label='Profit', zorder=5)

            # Plot the curved line
            plt.plot(x_new, y_new, color=color, linestyle='-', label='Curve Fit', zorder=4)

        # Add gridlines and labels
        plt.grid(True)
        plt.xlabel('Days')
        plt.ylabel('Profit')
        plt.title('Profit of the Month')
        plt.legend()
        plt.show()

# Example profits data for demonstration
monthly_profit_object = MonthlyProfit()

# Example datasets
dataset1 = [ProfitPoint(1, 100), ProfitPoint(2, 150), ProfitPoint(3, 200), ProfitPoint(4, 220)]
dataset2 = [ProfitPoint(1, 80), ProfitPoint(2, 130), ProfitPoint(3, 180), ProfitPoint(4, 200)]
dataset3 = [ProfitPoint(1, 120), ProfitPoint(2, 170), ProfitPoint(3, 220), ProfitPoint(4, 240)]

# Add datasets with different colors
monthly_profit_object.add_dataset(dataset1, color='blue')
monthly_profit_object.add_dataset(dataset2, color='green')
monthly_profit_object.add_dataset(dataset3, color='red')

# Plot the graph
monthly_profit_object.plot_profit_graph()
