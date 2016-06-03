import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)

def funkcija(x,y):
   return -np.cos(x)

y=0

for i in range(len(x)):
    k=funkcija(x[i],y)
    x=x+0.3
    y=y+k*0.3
    k.append(y)


k=(k1+k2)/2


plt.plot(x,k)
plt.show()


