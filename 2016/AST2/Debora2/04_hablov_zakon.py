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
import scipy.optimize  as curve_fit 

l, v, dv=np.loadtxt('hablov_zakon.dat', unpack=True)

plt.errorbar(l, v, yerr=dv, fmt='o')
plt.xlabel('udaljenost')
plt.ylabel('rad.brz')

def func(l,k,n):
    return k*l+n

parametri, cov_m=curve_fit(func, l, v, dv)

k=[0]
n=[1]

plt.show()
