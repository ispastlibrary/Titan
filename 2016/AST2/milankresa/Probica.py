import numpy as np
import pylab as pl
from scipy import interpolate
from scipy import integrate

file = np.loadtxt('podaci.txt')
L = file[:,0]
I = file[:,1]

spl = interpolate.splrep(L,I,k=3)
Lk = file[:,0]
Ik = spl(Lk)
pl.plot(Lk, Ik)
pl.show()
