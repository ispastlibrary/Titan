import numpy as np
import matplotlib.pyplot as plt

dx=1
x=np. arange(0, 10, 1)
y=np. zeros(len(x))
y[0]=0

for i in range(1, len(x)):
    y[i]=y[i-1] + (2*x[i]*dx)

















plt.plot(x,y)
plt.show()
