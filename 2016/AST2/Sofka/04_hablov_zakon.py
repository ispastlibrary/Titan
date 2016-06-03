"""
U file-u "hablov_zakon.dat" se nalaze podaci o udaljenosti galaksija
i njihovoj radijalnoj brzini, kao i greske za brzinu.

Vaš zadatak je da:
	1. Ucitate podatke iz file-a.
	2. Fitujete podatke linearnom funkcijom.
	3. Izracunate Hablovu konstantnu.
	4. Napravite grafik kao na slajdu.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, v, dv=np.loadtxt('hablov_zakon.dat', unpack = True)

def fun(n, p, o):
    return p*n+o

parametri,cov_m = curve_fit(fun, x, v, sigma=dv)
greske_parametara = np.sqrt(np.diag(cov_m))

c =  fun(x, parametri[0], parametri[1])

plt.plot(x,c, 'r-', label = 'linearan fit')
plt.errorbar(x, v, yerr = dv, fmt = 'o', label = 'podaci')

plt.xlabel('$D[Mpc]$')
plt.ylabel('$V_{rad}[km/s]$')
plt.ylim(-10000, 70000)
plt.xlim(0, 1000)

plt.legend(loc = 'best')
plt.show()

