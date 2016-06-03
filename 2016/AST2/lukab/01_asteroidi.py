"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np

a, l, i, e, x= np. loadtxt('asteroidi.dat', unpack=True)

S=0
for m in range(len(e)):
    if (i[m]>15) and (i[m]<70) and (x[m]>2.3):
        S=S+1
print(S)
