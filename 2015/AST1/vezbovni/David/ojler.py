import matplotlib.pyplot as plt
import numpy as np

dx=0.3
x = np.arange(0, 4*np.pi, dx)
y = np.zeros(len(x))
y[0]=0
for i in range (1, len(x)):
    k=-np.cos(x[i])
    y[i]=y[i-1]+k*dx

plt.plot(x, y, '-r')
plt.plot(x, -np.sin(x), '--b')
plt.show()
