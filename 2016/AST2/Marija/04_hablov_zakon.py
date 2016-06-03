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

a, b,c = np.loadtxt ("hablov_zakon.dat", unpack = True)

def func(a, d, f):
    return d*a+f

parametri,cov_m= curve_fit (func, a, b,sigma=c)
greske_parametara = np.sqrt (np.diag(cov_m))
y=func(a, parametri[0],parametri [1], )        


plt.plot(a, y, 'r-', label='linearan fit',)
plt.errorbar(a, b, yerr=c, fmt = 'o', label='podaci') 
plt.legend(loc='best')
plt.xlabel(r'$D[Mpc]$')
plt.ylabel(r'$v_{rad} [\frac{km}{s}]$')
plt.xlim(0,1000)
plt.ylim(-10000,70000)
plt.show()

