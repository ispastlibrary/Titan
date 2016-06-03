"""
U file-u "hablov_zakon.dat" se nalaze podaci o udaljenosti galaksija
i njihovoj radijalnoj brzini, kao i greske za brzinu.

Vaš zadatak je da:
	1. Ucitate podatke iz file-a.
	2. Fitujete podatke linearnom funkcijom.
	3. Izracunate Hablovu konstantnu.
	4. Napravite grafik kao na slajdu.
"""
import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

x, v, dv = np.loadtxt("hablov_zakon.dat", unpack = True)

plt.plot(x, v, 'ob', label = 'habl', )
plt.xlim(0,1100)
plt.ylim(-10000,80000)
plt.errorbar(x,v, yerr=dv, fmt = 'o')
def func(x,a,c):
    return a*x+c
parametri, cov_m = curve_fit(func, x, v, sigma = dv)
greske_parametara = np.sqrt(np.diag(cov_m))

y = func(x,parametri[0], parametri[1])
plt.show(x,y)
plt.show()


