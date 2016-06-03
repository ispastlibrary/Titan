import numpy as np
import matplotlib.pyplot as plt

dx = 0.4
x=np. arange(1,4,dx)
y=np.zeros(len(x))
y[0]=np. e


for i in range(1, len(x)):
    y[i]=y[i-1] + ((np. e**x[i])*dx)

plt.plot(x,y,'-r')
y1=np. e**x
plt.plot(x,y1,'-b')
plt.show()
