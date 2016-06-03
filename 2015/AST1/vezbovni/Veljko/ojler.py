import numpy as np
import matplotlib.pyplot as plt

x = np.arange (0, np.pi*4, 0.3)
dx = 0.3
y = np.zeros(len(x))
y[0] = 0 

for i in range(1, len(x)):

    y[i] = y[i-1] -dx *np.cos(x[i])
    

plt.plot(x, y, '-r', label = 'fit')
plt.plot(x, -np.sin(x), '-b', label = 'fit')
plt.show()

