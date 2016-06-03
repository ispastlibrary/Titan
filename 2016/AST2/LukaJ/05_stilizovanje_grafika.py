"""
Trebate da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.interpolate import interp1d
X, Y = np.loadtxt('stilizovanje_grafika.dat', unpack = True)

flin = interp1d(X, Y, kind='linear')
fcub = interp1d(X, Y, kind='cubic')

Mnogox = np.linspace(X.min(), X.max(), num = 1000)

y1 = flin(Mnogox)
y2 = fcub(Mnogox)


plt.plot(Mnogox, y1)
plt.plot(Mnogox, y2, 'r--')
plt.show()

