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

def func(x, k, n):
    return k*x + n

x, x1, x2 = np.loadtxt('hablov_zakon.dat', unpack = True)

parametri, cov_m = curve_fit(func, x, x1, sigma = x2)
greske_parametara = np.sqrt(np.diag(cov_m))

print(parametri[0], parametri[1])
plt.scatter(x, x1)
plt.plot(x, func(x,parametri[0],parametri[1]))
plt.xlabel('D[Mpc]')
plt.ylabel('V[km/s]')
plt.errorbar(x, x1, yerr=x2, ls = 'none')
plt.show()
