import numpy as np
import pyplot as pl
from scipy import interpolate
from scipy import integrate

file = np.loadtxt('podaci.txt')
L = file[:,0]
I = file[:,1]

spl = interpolate.splrep(L,I,k=3)
Lk = file[:,0]
Ik = spl(xs)
pl.plot(xs, ys)
pl.show()
