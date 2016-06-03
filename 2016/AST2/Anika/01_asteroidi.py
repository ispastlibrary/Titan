"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np

p,l,i,e,a = np.loadtxt('asteroidi.dat', unpack=True)

brojac=0

for k in range(len(i)):
    if (a[k]>2.3) and (i[k]>15) and (i[k]<70):
        brojac+=1

print(brojac)
