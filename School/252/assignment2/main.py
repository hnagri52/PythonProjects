import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.arange(-3, 3, 0.01)

    plt.plot(t, np.exp(-2 * (1 + 1j * np.pi) * t).imag)
    plt.xlabel('t')
    plt.ylabel('Im x(t)')
    plt.title(r'Imaginary part of  $x(t)=e^{-2j \pi t}$')
    plt.xlim([-10,10])
    plt.show()


if __name__ == '__main__':
    plot_graph()