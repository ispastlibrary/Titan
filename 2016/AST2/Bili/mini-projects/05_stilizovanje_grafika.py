"""
Trebate da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x, y = np.loadtxt('stilizovanje_grafika.dat', unpack = True)
l=interp1d(x, y, kind ='linear')
c=interp1d(x, y, kind='cubic')
#plt.scatter(x, y)
x1=np.linspace(1,11, num=41, endpoint=True)
plt.plot(x, y, 'o', x1, l(x1), '-',  x1, c(x1), '--')
plt.legend(['data', 'linear', 'cubic'], loc = 'best')
#plt.set_yticks(y, minor = False)
plt.grid(True)
plt.show()

