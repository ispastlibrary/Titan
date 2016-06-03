"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np

inklinacija, velikapol = np.loadtxt("asteroidi.dat", usecols=(2, 4), unpack=True)
asteroidi=0
for i in range (len(inklinacija)):
    if (inklinacija[i]<70) and (inklinacija[i]>15) and (velikapol[i]>2.3):
        asteroidi = asteroidi + 1
    
    
print (asteroidi)
