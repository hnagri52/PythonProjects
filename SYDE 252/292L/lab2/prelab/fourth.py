import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(100, 10000)

    plt.semilogx(t, np.arctan(1/(2*np.pi*t*4700*0.033*pow(10, -6))) *180/np.pi)
    plt.xlabel('Frequency')
    plt.ylabel('gain (dB)')
    plt.title("Frequency of variation vs phase shift")
    plt.xlim([100, 10000])

    plt.show()


if __name__ == '__main__':
    plot_graph()