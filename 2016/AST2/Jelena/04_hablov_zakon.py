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

d,v,dv = np.loadtxt("hablov_zakon.dat",unpack=True)


plt.plot(d,v,'og')
plt.errorbar(d,v,dv)
plt.show()

def fit(d,a,b):
    return 


