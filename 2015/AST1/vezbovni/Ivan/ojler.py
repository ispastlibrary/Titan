import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0, 20, 0.3)
y0=0
dx=0.3
def k1(x, y):
    return -np.cos(x)
lista= []
for i in range(len(x)):
    y = y0 + (-np.cos(x[i]))*dx
    lista.append(y)
    y0=y

plt.plot(x, lista)
plt.show()
