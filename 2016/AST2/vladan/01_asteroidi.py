"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np

x1,x2,x3,x4,x5 = np.loadtxt('asteroidi.dat', unpack=True)

broj=0
i=0

while i < len(x1):
    if (15< x3[i]<70) and (x5[i]>2.3):
        broj+=1
    i+=1

print(broj)
