"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""

import numpy as np
AP, LUC, I, E, A = np.loadtxt('asteroidi.dat', unpack = True)

j = 0

for k in range(len(I)):
    if 15 < I[k] < 70 and A[k]>2.3:
        j = j + 1

print(j)
