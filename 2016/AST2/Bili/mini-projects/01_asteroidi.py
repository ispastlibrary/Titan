"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np
k=0
x1,x2,x3,x4,x5=np.loadtxt("asteroidi.dat",unpack=True)
print(x1)
for i in range(len(x1)):
    if ((x3[i]>15) and (x3[i]<70) and (x5[i]==2.3)):
        k+=1  
print(k)
