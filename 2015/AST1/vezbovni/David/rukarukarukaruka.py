import matplotlib.pyplot as plt
import numpy as np

dx=0.3
x = np.arange(0, 20, dx)
y = np.zeros(len(x))
k = np.zeros(3)
y[1]=0
for i in range (1, len(x)):
    k[0]=-np.cos(x[i-1])
    y[i] = y[i-1]+k[0]*dx
 
    k[1]=-np.cos(x[i])
    y[i+1] = y[i]+k[1]*dx
    
    k[2]=(k[0]+k[1])/2
    y[i]=y[i-1]+k[2]*dx

plt.plot(x, y, '-r')
plt.plot(x, -np.sin(x), '--b')
plt.show()
