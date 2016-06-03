from scipy.special import wofz
import numpy as np

def voigt(x,y):
    z=x+1j*y
    w=wofz(z).real
    return w

print(voigt(0,0.002)/np.sqrt(np.pi))
