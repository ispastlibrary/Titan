import numpy as np
import matplotlib.pyplot as plt

dx = 0.4
x = np.arange(0, 4, dx)
y = np.zeros(len(x))
y[0]=1
for i in range (len(x)):
    k=np.exp(x[i])
    y[i]=y[i-1]+k*dx

plt.plot(x, y, '-r')
plt.plot(x, np.exp(x), '--b')
plt.show()
