
#"""
#Prebrojte koliko asteroida iz file-a "asteroidi.dat" ima inklinaciju
#izmedju 15 i 70 stepena i veliku poluosu duzu od 2.3 AJ.

#Podaci u file-u su rasporedjeni po kolonama:
#argument perihela [deg] | longituda uzlaznog cvora [deg] | inklinacija (i) [deg] | ekscentricitet (e) | velika poluosa (a) [AJ]
#"""
import numpy as np

A, L, I , E, V=np.loadtxt('asteroidi.dat', unpack=True)

a=0
for a in (A):
	if (V[i]> 2.3) and (15<I[i]) and (I<70[i]):
		a +=1
print(a)

plt.show()

