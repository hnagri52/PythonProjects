import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(0, 12)

    plt.plot(t, t-t+4, label="Marginal Revenue", color="red")
    plt.plot(t, (1/4)* pow((t-3),2) + 3, label="Marginal Cost", color="blue")
    plt.plot(t, (1/8)* pow((t-3),2) + 5, label="Average Total Cost", color="green")
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.title(r'Competitive market: Negative Economic Profit')
    plt.xlim([0,12])
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    plot_graph()
