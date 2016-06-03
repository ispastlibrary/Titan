"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np
a,b,c,d,e=np.loadtxt('asteroidi.dat', unpack=True)
s=0
for i in range(len(c)):
	if (c[i]>15) and (c[i]<70) and e[i]>2.3 :
		s+=1
print(s)

	
