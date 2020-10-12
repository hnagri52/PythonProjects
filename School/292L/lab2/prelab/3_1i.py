import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(0.1, 10000)
    # t = np.linspace(-10, 10, 1000)

    plt.semilogx(t, 20 * np.log10( (10000) / (np.sqrt(pow(235 * t, 2) + 110250000 )) ))
    plt.xlabel('w(rad/s)')
    plt.ylabel('Gain (db)')
    plt.xlim([0.1, 10000])
    # plt.grid()
    plt.show()


if __name__ == '__main__':
    plot_graph()