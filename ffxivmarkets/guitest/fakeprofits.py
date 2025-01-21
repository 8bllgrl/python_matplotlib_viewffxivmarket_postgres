import matplotlib.pyplot as plt
import numpy as np

def plot_profit_graph(profits):
    x = np.arange(len(profits))
    y = profits

    # Fit a curve to the points
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    x_new = np.linspace(x[0], x[-1], 100)
    y_new = f(x_new)

    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, color='blue', label='Profit', zorder=5)
    plt.plot(x_new, y_new, color='green', linestyle='-', label='Curve Fit', zorder=4)

    plt.grid(True)
    plt.xlabel('Days')
    plt.ylabel('Profit')
    plt.title('Profit of the Month')
    plt.legend()
    plt.show()

# Example profits data for demonstration
profits = [100, 150, 200, 220, 250, 280, 300, 320, 350, 400, 420, 450, 480, 500, 520, 550, 580, 600, 620, 650, 680, 700, 720, 750, 780, 800, 820, 850, 880, 900]

# Plot the graph
plot_profit_graph(profits)
