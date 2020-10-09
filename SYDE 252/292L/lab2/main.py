import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(0, 10000)
    # t = np.linspace(-10, 10, 1000)

    plt.semilogx(t, -10 * np.log10(1 + np.power(2*np.pi*t*4700*0.033*pow(10, -6),2)))
    plt.xlabel('t')
    plt.ylabel('Im x(t)')
    # plt.title(r'Imaginary part of  $x(t)=e^{-2(1+ j \pi)t}$')
    plt.xlim([0,10000])

    plt.show()


if __name__ == '__main__':
    plot_graph()