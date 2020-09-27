import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    t = np.linspace(-10, 10, 1000)
    # plt.subplot(2, 1, 1);
    # plt.plot(t, np.exp(-2j * np.pi * t).real);
    # plt.xlabel('t');
    # plt.ylabel('Re x(t)');
    # plt.title(r'Real part of  $x(t)=e^{-2j \pi t}$');
    # plt.xlim([-10, 10]);

    # plt.subplot(2, 1, 2);
    plt.plot(t, -1 * np.exp(-2 * t) * (1j * np.sin(2 * np.pi * t)).imag);
    plt.xlabel('t');
    plt.ylabel('Im x(t)');
    plt.title(r'Imaginary part of  $x(t)=e^{-2j \pi t}$');
    plt.xlim([-11,10]);
    plt.show()


if __name__ == '__main__':
    plot_graph()