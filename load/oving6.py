import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




A = 800

mju = 13

sigma = 3

t = np.linspace(0, 24, 500)


G_t = A * np.exp(-((t - mju)**2) / (2 * sigma**2))

plt.plot(t, G_t)
plt.xlabel("Tidspunkt (timer)")
plt.ylabel("Innstråling")
plt.title("Solinstråling")
plt.grid()
plt.show()