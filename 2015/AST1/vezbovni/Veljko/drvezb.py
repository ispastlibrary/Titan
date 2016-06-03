import matplotlib.pyplot as plt
import numpy as np


Ctg, Pc = np.loadtxt('podaci3.txt', unpack = True)
dlam, lam, c =np.loadtxt('podaci2.txt', unpack = True)

def fun(dlam, lam, c)
    return((dlam/lam)*c)

def fun1(Ctg, Pc)
    return(Ctg*Pc)


