import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.interpolate import interp1d
x,y = np.loadtxt("linija.dat", unpack = True)

#linear
Xl=[]
Yl=[]
fl=interp1d(x,y)
for i in range(0,99):
    xnewl=np.arange(x[i],x[i+1],(x[i+1]-x[i])/6)
    ynewl=fl(xnewl)
    for j in range(0,6):
        Xl.append(xnewl[j])
        Yl.append(ynewl[j])
        j +=1
    i +=1
Xl.append(x[99])
Yl.append(y[99])
h=(x[99]-x[0])/595
S=0
#Simspson
for n in range(2,595):
    S=S+h/3*(Yl[n-2]+Yl[n-1]+Yl[n])
    n +=2
print('Moj Simpson i linearna interpolacija:',x[99]-x[0]-S)
#cubic
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
s=simps(Yc,Xc)
print('SciPy.simps i cubic:',x[99]-x[0]-s)

yc = np.asarray(Yc)

plt.plot(Xl,Yl,'.',label='Linearna interpolacija')
plt.plot(Xc,yc-0.3,'.',label='Kubna interpolacija')
plt.plot(x,y-0.6,'.',label='Ulazni podaci')
plt.legend(loc='best')
plt.show()
