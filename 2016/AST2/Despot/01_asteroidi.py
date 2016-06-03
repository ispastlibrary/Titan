"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""

import numpy as np

n = 0

per,long,ink,eks,poluosa = np.loadtxt('asteroidi.dat', unpack = True)

for j in range(len(per)):
    if  (ink[j] > 15) and (ink[j] < 70) and (poluosa[j] > 2.3):
        n += 1

print("Postoji", n ,"takvih asteroida. ")
