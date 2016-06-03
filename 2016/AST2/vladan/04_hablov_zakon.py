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

def f(x,a,b):
    return a*x+b

x, y, greske_po_y = np.loadtxt('hablov_zakon.dat', unpack=True)

parametri, cov_m = curve_fit(f, x, y, sigma=greske_po_y)
greske_parametara = np.sqrt(np.diag(cov_m))

plt.plot(x, y)
plt.errorbar(x,y,yerr=greske_po_y,fmt='o')
plt.show()
