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
l, vr, deltav = np.loadtxt("hablov_zakon.dat", unpack=True)
def fun (l, a, b):
    return a*l+b    
plt.plot(l, vr,'ob') 
plt.errorbar(l, vr, yerr=deltav,fmt='o' )
parametri, cov_m = curve_fit(fun,l,vr,sigma=deltav)
y=fun(l, parametri[0], parametri[1])
plt.plot(l, y) 
plt.show()

