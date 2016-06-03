import numpy as np
import matplotlib.pyplot as plt
import math

n = 10000

x = np.random.rand(n)
y = np.random.rand(n)
q = 0

for i in range(n):
    if ((x[i]**2 + y[i]**2)**(0.5)<1):
        plt.scatter(x[i],y[i],c='b')
        q += 1
    else:
        plt.scatter(x[i],y[i],c='r')
Pi = 4*q/n


plt.show()
print(Pi)

