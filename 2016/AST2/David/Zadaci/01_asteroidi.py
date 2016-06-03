"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as numpu
ap, long, ink, eksc, vpa = numpu.loadtxt('asteroidi.dat', unpack = True)

i = 0
for ch in range(len(ap)):
	if ((ink[ch]<=70) and (ink[ch] >= 15) and (vpa[ch] > 2.3)):
		i=i+1
print(i)
		
