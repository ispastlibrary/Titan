"""
#Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
#izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

#Podaci u file-u su rasporedjeni po kolonama:
#argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np 
a, b, c, d,e=np.loadtxt("asteroidi.dat",unpack=True)
i=0

for j in range (len(a)):
    if (c[j]<70) and (c[j]>15) and (e[j]>2.3):
        i+=1
print(i)
