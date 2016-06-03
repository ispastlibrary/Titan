
"""
Trebate da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp1d

x,y=np.loadtxt('stilizovanje_grafika.dat', unpack=True)

f=interp1d(x,y,'-r', kind='linear')
f2=interp1d(x,y, kind='kubic')
k=np.linspace(x[0], x[len(x)-1], num=101)
l=f(k)

plt.plot(x,y, label='Primer stilizovanja grafika sa interpolacijom')
plt.plot(k,l)
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.grid()
plt.legend(loc='best')


plt.show()
