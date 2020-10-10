import matplotlib.pyplot as plt
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]

vals = [
    -5.52616848,
    -11.03884056,
    -16.27336116,
    -21.2429448,
    -25.98049603,
    -30.34370247,
    -34.38560760,
    -37.99551711,
    -41.23287844,
    -44.21441049,
    -62.87198638,
    -75.65204347,
    -84.17596772,
]


# plot, show, and label the graph
plt.title("Frequency vs phase shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase")
plt.semilogx(x, vals, marker = ".",
             markersize = 8)

# plt.grid(True)
plt.show()
