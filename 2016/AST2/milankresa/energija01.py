from numpy import *
import pylab

a, x1, P, T, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25 = loadtxt('energy.txt', unpack=True)

pylab.plot(a,P)
pylab.plot(a,T)

pylab.show()
