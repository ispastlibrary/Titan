import numpy as np
import matplotlib.pyplot as plt

z=np.arange(0, 10, 0.02)
d=[]

pi=3.141592653
def m(z, y):
    return -np.cos(z)

y0 = 0
x0 = 0
k = m(x0, y0)

for i in range(len(z)):
    y=y0+(-np.cos(z[i]))*0.3
    d.append(y)
    y0=y

plt.plot(z, d)
plt.show()
