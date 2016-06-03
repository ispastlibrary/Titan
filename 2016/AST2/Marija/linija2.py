import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.interpolate import interp1d
x,y = np.loadtxt("linija.dat", unpack = True)


Xc=[]
Yc=[]
fc=interp1d(x,y,kind='cubic')

for i in range(0,99):
    xnewc=np.arange(x[i],x[i+1],(x[i+1]-x[i])/6)
    ynewc=fc(xnewc)
    for j in range(0,6):
        Xc.append(xnewc[j])
        Yc.append(ynewc[j])
        j +=1
    i +=1
Xc.append(x[99])
Yc.append(y[99])
plt.plot(Xc,Yc,'o')
plt.show()
s=simps(Yc,Xc)
print(x[99]-x[0]-s)
