"""
Treba da napravite grafik koji ce izgledati kao onaj na slajdu.

Podatke ucitajte iz file-a "stilizovanje_grafika.dat"
"""


import numpy as np
import matplotlib.pyplot as plt


x, y= np.loadtxt("stilizovanje_grafika.dat", unpack=True)
plt.scatter(x,y)
plt.plot(x,y,'--b')
plt.show()
