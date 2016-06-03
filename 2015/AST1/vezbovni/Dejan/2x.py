import numpy as np
import matplotlib.pyplot as plt

dx=1
x=np. arange(0, 5, 1)
y=np. zeros(len(x))
y[0]=0
y1=x**2

for i in range (1, len(x)):
    y[i]=y[i-1] + (2*x[i]*dx)

plt.plot(x,y,'-r')
plt.plot(x,y1,'-b')
plt.show()    
