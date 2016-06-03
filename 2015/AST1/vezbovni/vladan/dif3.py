import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 8, 0.3)
y = [0]

for i in range(1, len(x)):
    k1 = (-1)*np.cos(x[i])
    k2 = (-1)*np.cos(x[i]+0.15)
    k3 = (-1)*np.cos(x[i]+0.3)
    k = (k1 + 4*k2 + k3)/6
    y.append(y[i-1] + k*0.3)

plt.plot(x, y)
plt.show()
