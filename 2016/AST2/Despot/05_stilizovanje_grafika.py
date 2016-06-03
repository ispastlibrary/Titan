"""
Trebate da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

x, y = np.loadtxt('stilizovanje_grafika.dat', unpack = True)

flin = interp1d(x , y , kind = 'linear')
fcub = interp1d(x , y , kind = 'cubic')
#y = f(a)

int_x = np.linspace(x.min(), x.max(), num = 111)
lin_y = flin(int_x)
cub_y = fcub(int_x)

plt.plot(int_x , lin_y , 'g-')
plt.plot(int_x , cub_y , 'r-.')
plt.grid()
plt.show()
