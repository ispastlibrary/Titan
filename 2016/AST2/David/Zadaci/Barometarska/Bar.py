import numpy as brojpit
import matplotlib.pyplot as slika
import scipy as naukpit

x,y,greska = brojpit.loadtxt("barometarska.txt", unpack = True, delimiter = " ")
slika.plot(x,y, 'om')
slika.errorbar(x,y,yerr = greska,fmt = None ,color = 'm')

xij = []
for jj in range(35000):
    xij.append(jj/100)
apocetno = 0
bpocetno = 0
hi = 100

for i in range(100):
    a = apocetno+0.01*i
    for jot in range(100):
        b = bpocetno+0.001*jot
        his = 0
        for nesto in range(len(x)):
            his = his + ((y[nesto]-a*2.718**(-b * x[nesto]))/2**0.5*greska[nesto])**2
        if(hi>his):
            hi = his
            afinal = a
            bfinal = b
print(afinal)
print(bfinal)
#slika.plot(xij, afinal*2.718**(-bfinal*xij), 'm')
slika.show()

