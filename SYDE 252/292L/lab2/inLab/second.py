import matplotlib.pyplot as plt
import numpy as np
from math import e
import math
import cmath

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]

vals = [
-20.26583041,
-14.36787166,
-11.04633766,
-8.787487393,
-7.160245564,
-5.932174569,
-4.961267372,
-4.211672211,
-3.618160501,
-3.126976245,
-1.013827599,
-0.2749897998,
-0.04647331485,

]


# plot, show, and label the graph
plt.title("Simulated Gain vs phase shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.semilogx(x, vals, marker = ".",
             markersize = 8)

# plt.grid(True)
plt.show()
