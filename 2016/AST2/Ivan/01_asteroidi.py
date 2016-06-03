"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""

import numpy as np
ap, luc, i, e, a = np.loadtxt('asteroidi.dat', unpack=True)

broj=0

for j in range(len(ap)):
    if (i[j]>=15 and i[j]<=70 and a[j]>2.3):
        broj=broj+1
print(broj)
