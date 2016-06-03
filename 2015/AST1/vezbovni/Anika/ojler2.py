import numpy as np
import matplotlib.pyplot as plt

dx=0.3
x=np.arange(1, np.pi*4, dx)
y=np.zeros(len(x))

y[0]=1

for i in range(1, len(np.exp(x))):
    y[i]=y[i-1]+((np.exp(x[i]))*dx)

plt.plot(x, y, '-r')
plt.plot(x, np.exp(x), '-b')
plt.show()

