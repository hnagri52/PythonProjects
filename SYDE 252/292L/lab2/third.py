import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(100, 10000)

    plt.semilogx(t, -1 * np.arctan(2*np.pi*t*4700*0.033*pow(10, -6)) *180/np.pi)
    plt.xlabel('t')
    plt.ylabel('PLOT x(t)')
    plt.xlim([100, 10000])

    plt.show()


if __name__ == '__main__':
    plot_graph()