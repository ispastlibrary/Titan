import numpy as np
import matplotlib.pyplot as plt

dx=0.3
x=np.arange(0, np.pi*4, dx)
y=np.zeros(len(x))

y[0]=0

for i in range(1, len(x)):
    y[i]=y[i-1]+(-1*np.cos(x[i])*dx)

plt.plot(x, y, '-r')
plt.plot(x, -np.sin(x), '-b')
plt.show()
