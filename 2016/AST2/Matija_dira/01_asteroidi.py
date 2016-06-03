"""
Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

Podaci u file-u su rasporedjeni po kolonama:
argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
"""
import numpy as np
AP,LUC,IN,EX,VPO=np.loadtxt("asteroidi.dat",unpack=True);
n=0;
for i in range(len(AP)):
    if(IN[i]>15 and IN[i]<75 and VPO[i]>2.3):
        n+=1;
print(n); 
