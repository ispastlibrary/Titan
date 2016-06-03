"""
U file-u "hablov_zakon.dat" se nalaze podaci o udaljenosti galaksija
i njihovoj radijalnoj brzini, kao i greske za brzinu.

Vaš zadatak je da:
	1. Ucitate podatke iz file-a.
	2. Fitujete podatke linearnom funkcijom.
	3. Izracunate Hablovu konstantnu.
	4. Napravite grafik kao na slajdu.
"""
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

d, w, R = np.loadtxt('hablov_zakon.dat', unpack = True)


plt.errorbar(d, w, yerr = R, fmt='o')

def fun(x,A,B):
    return A*x + B


parametri, cov_m = curve_fit(fun, d, w, sigma = R)
greske = np.sqrt(np.diag(cov_m))

y = fun(d, parametri[0], parametri[1])

plt.plot (d, y)

plt.show()
