import matplotlib.pyplot as plt
x = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

vals = [
-0.1948863492,
-0.2102951882,
-0.2171954394,
-0.247948636,
-0.2891568947,
-1.706531323,
-4.465229627,
-16.57853766,
-22.49252222
]


# plot, show, and label the graph
plt.title("Frequency vs gain ")
plt.xlabel("frequnecy")
plt.ylabel("gain (dB)")
plt.semilogx(x, vals, marker = ".",
             markersize = 8)

# plt.grid(True)
plt.show()