import matplotlib.pyplot as plt
import numpy as np

class ProfitPoint:
    def __init__(self, day, profit):
        self.day = day
        self.profit = profit

class ProfitDataset:
    def __init__(self, name):
        self.name = name
        self.points = []
        self.color = None

    def add_point(self, day, profit):
        self.points.append(ProfitPoint(day, profit))

    def set_color(self, color):
        self.color = color

class MonthlyProfit:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, dataset):
        self.datasets.append(dataset)

    def plot_profit_graph(self):
        # Set the figure size to be wider
        plt.figure(figsize=(12, 6))  # Adjust the width and height as needed

        for dataset in self.datasets:
            days = [point.day for point in dataset.points]
            profits = [point.profit for point in dataset.points]

            # Fit a curve to the points
            z = np.polyfit(days, profits, 3)
            f = np.poly1d(z)
            x_new = np.linspace(min(days), max(days), 100)
            y_new = f(x_new)

            # Plot the original points
            plt.scatter(days, profits, color=dataset.color, label=dataset.name, zorder=5)

            # Plot the curved line
            plt.plot(x_new, y_new, color=dataset.color, linestyle='-', label='Curve Fit', zorder=4)

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
dataset1 = ProfitDataset("Dataset 1")
dataset1.add_point(1, 100)
dataset1.add_point(2, 150)
dataset1.add_point(3, 200)
dataset1.add_point(4, 220)
dataset1.set_color('blue')

dataset2 = ProfitDataset("Dataset 2")
dataset2.add_point(1, 80)
dataset2.add_point(2, 130)
dataset2.add_point(3, 180)
dataset2.add_point(4, 200)
dataset2.set_color('green')

dataset3 = ProfitDataset("Dataset 3")
dataset3.add_point(1, 120)
dataset3.add_point(2, 170)
dataset3.add_point(3, 220)
dataset3.add_point(4, 240)
dataset3.set_color('red')

# Add datasets
monthly_profit_object.add_dataset(dataset1)
monthly_profit_object.add_dataset(dataset2)
monthly_profit_object.add_dataset(dataset3)

# Plot the graph
monthly_profit_object.plot_profit_graph()
