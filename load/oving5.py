import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



L_0 = 10000

A_i = 1500

mju_i = 16

sigma_i = 4

t = np.linspace(0, 24, 500)


L_t = L_0 + A_i * np.exp(-((t - mju_i)**2) / (2 * sigma_i**2))

plt.plot(t, L_t)
plt.xlabel("Tidspunkt (timer)")
plt.ylabel("Last")
plt.title("Gauss-modell")
plt.xticks(range(0, 25 ,2))
plt.grid()
plt.show()