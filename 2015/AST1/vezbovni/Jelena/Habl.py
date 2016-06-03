import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
D, V, dV = np.loadtxt('merenja_habla.txt', unpack = True)

def fun(x, a, b):
    return x * a + b
par, cov = curve_fit(fun, D, V, sigma=dV)
# par[0] - a sto je u ovom slucaju koeficijent pravca; par [1] - b ;; 
dpar = np.sqrt(np.diag(cov))
#dpar su greske parametara (a,b)

a = par[0]
b = par[1]
print(a, 'Ovo je a')
print(b, 'Ovo je b')
mD = (1.2, 1.8, 0.05)
mV = fun(mD, a, b)
print(cov, 'Ovo je matrica greske')
print(mD) 
print(mV, 'ovo je v ')
