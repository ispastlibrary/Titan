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

x,y,dy=np.loadtxt("hablov_zakon.dat", unpack=True)
def funkcija(x,a,b):
    return a*x+b
parametri,cov_m=curve_fit(funkcija, x,y,sigma=dy)
greskep=np.sqrt(np.diag(cov_m))
plt.errorbar(x,y, yerr=dy, fmt='o', label='podaci')
y=funkcija(x,parametri[0],parametri[1])
plt.xlabel('d[Mpc]')
plt.ylabel('V[km/s]')
plt.title('Zavisnost radijalne brzine od udaljenosti')
plt.plot(x,y, '-r', label='linearni fit')
plt.legend(loc='best')
plt.show()
print(parametri[0])
