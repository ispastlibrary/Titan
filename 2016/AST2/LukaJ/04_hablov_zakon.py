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

R, V, L = np.loadtxt('hablov_zakon.dat', unpack = True)

def func(x, A, B):
    return A*x + B

plt.errorbar(R, V, yerr = L, fmt='o')
parametri, cov_m = curve_fit(func, R, V, sigma = L)
greska = np.sqrt(np.diag(cov_m))

y = func(R, parametri[0], parametri[1])


plt.plot(R, y)
plt.show()

