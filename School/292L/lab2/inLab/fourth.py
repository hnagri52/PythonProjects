import matplotlib.pyplot as plt
x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]

vals = [
    84.43279587,
    78.91751361,
    73.77628297,
    68.71736124,
    64.07386837,
    59.69083856,
    55.62875661,
    52.00298186,
    48.73476489,
    45.70371647,
    27.10801595,
    14.37596602,
    5.854496417
]


# plot, show, and label the graph
plt.title("Frequency vs phase shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase")
plt.semilogx(x, vals, marker = ".",
             markersize = 8)

# plt.grid(True)
plt.show()
