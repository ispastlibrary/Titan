

import numpy as np
x=np.arange(0,10,0.1)
import matplotlib. pyplot as plt

def funkcija(x,y):
    return -np.cos(x)
y0=0
x0=0
k=funkcija(x0,y0)
print(k)

y=0
z=[]
#x=np.linspace(0,10,num=10)
for i in range(len(x)):
    y=y+0.3*funkcija(x[i],y)
    z.append(y)   

plt.plot(x,z)
plt.show()

 
    
