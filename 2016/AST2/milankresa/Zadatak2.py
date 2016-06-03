import numpy as np
import pylab as pl 
from scipy import interpolate

file = np.loadtxt('podaci.txt')
L = file[:,0]
I = file[:,1]
xclanovi = []
yclanovi = []
Lp = []
Ip = []

data = interpolate.splrep(L,I,k=3)
Is=interpolate.splev(L,data,der=0)
pl.plot(L,Is,'blue', label='Cubic spline', linewidth=2)

for i in range(0, len(L)-1):
    dL = (L[i+1]-L[i])/6
    X = L[i]
    for n in range(0, 6):
          X = X+ dL
          Y = I[i]+((I[i+1]-I[i])*(X-L[i]))/(L[i+1]-L[i])
          xclanovi.append(X)
          yclanovi.append(Y)

#xclanovi.append(L[0])
#yclanovi.append(I[0])

Lp = list(xclanovi)
Ip = list(yclanovi)

Lp.sort()
Ip.sort()

P = 0
P1 = 0

for k in range(0, len(Lp)-1):
    srednje = Ip[k]+((Ip[k+1]-Ip[k])*(((Lp[k+1]+Lp[k])/2)-Lp[k]))/(Lp[k+1]-Lp[k])
    P = P + ((Lp[k+1]-Lp[k])/6)*(Ip[k]+4*srednje+Ip[k+1])
    P1 = P1 + interpolate.splint(Lp[k],Lp[k+1],data)
    

P = (L[len(L)-1]-L[0])-P
P1 = (L[len(L)-1]-L[0])-P1

print('Numericka integracija: ',P,' Numericka integracija Scipy: ', P1)

pl.plot(xclanovi, yclanovi, 'red', label='Linearna interpolacija')
pl.scatter(L,I,color='orange', label='Dobijeni podaci') 
pl.ylim(0.75,1.05)
pl.xlim(5395.30,5396.5)
pl.xlabel('Talasna dužina')
pl.ylabel('Fluks zračenja')
pl.legend(loc='best')
pl.show()

    

