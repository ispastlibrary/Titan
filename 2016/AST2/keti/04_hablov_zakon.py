""" U file-u "hablov_zakon.dat" se nalaze podaci o udaljenosti galaksija
i njihovoj radijalnoj brzini, kao i greske za brzinu.

Vaš zadatak je da:
	1. Ucitate podatke iz file-a.
	2. Fitujete podatke linearnom funkcijom.
	3. Izracunate Hablovu konstantnu.
	4. Napravite grafik kao na slajdu."""
import numpy as np
import matplotlib.pyplot as plt

udaljenost, brzina, brzinaerr = np.loadtxt('hablov_zakon.dat', unpack=True)
plt.errorbar(udaljenost, brzina, yerr=brzinaerr, fmt='o')

def func(x, m, b):
    return m*x+b
xnovo = np.linspace(0, 1000, 10000)
from scipy.optimize import curve_fit
parametri, cov_m = curve_fit(func, udaljenost, brzina, sigma=brzinaerr)
ynovo = func(xnovo, parametri[0], parametri[1])
greske_parametara = np.sqrt(np.diag(cov_m))
plt.plot(udaljenost, brzina, 'o', xnovo, ynovo)
plt.show()
