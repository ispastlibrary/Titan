#"""
#Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
#izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

#Podaci u file-u su rasporedjeni po kolonama:
#argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
#"""

import numpy as np

AP, Long, Inc, Exc, Vp=np.loadtxt("asteroidi.dat", unpack = True);

n = 0

for i in range (len(AP)):
    if (Inc[i] > 15) and (Inc[i] < 70) and (Vp[i] > 2.3):
        n += 1
print(n) 
