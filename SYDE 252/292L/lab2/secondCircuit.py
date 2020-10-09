import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(100, 10000)

    plt.semilogx(t, 20 * np.log10(4700 / np.sqrt(pow(4700, 2) + np.power(1/(2*np.pi*t*0.033*pow(10, -6)), 2))))
    plt.xlabel('t')
    plt.ylabel('PLOT x(t)')
    plt.xlim([100,10000])

    plt.show()


if __name__ == '__main__':
    plot_graph()