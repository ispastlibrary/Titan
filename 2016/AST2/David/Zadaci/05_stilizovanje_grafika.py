"""
Trebate da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


x,y = np.loadtxt("stilizovanje_grafika.dat", unpack = True)
f = interp1d(x, y)
f2 = interp1d(x, y, kind = 'cubic')

xnew = np.linspace(1, 11, num = 41, endpoint = True)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc = 'best')
plt.show()
