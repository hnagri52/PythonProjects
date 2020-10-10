import matplotlib.pyplot as plt
import numpy as np
from math import e
import math
import cmath

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 10000]

vals = [
    -0.04397338882 ,
    -0.1619289681 ,
    -0.3561926939 ,
    -0.6143455235 ,
    -0.9236242305 ,
    -1.276197242 ,
    -1.658784638 ,
    -2.061017421 ,
    -2.477449394 ,
    -2.898176765 ,
    -6.810332369 ,
    -12.09076787 ,
    -19.81238707
]


# plot, show, and label the graph
plt.title("Simulated Gain vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.semilogx(x, vals, marker = ".",
             markersize = 8)

# plt.grid(True)
plt.show()
