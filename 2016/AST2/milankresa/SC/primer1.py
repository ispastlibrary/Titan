import matplotlib.pyplot as plt
import numpy as np
from scipy.misc  import derivative

def parc_izvod(func, var, point=[]):
    args = point[:]
    def wraps(x):
        args[var]=x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)

def x   
    
def fja(x,y):
    z = x**2 + y**2
    return z


L=parc_izvod(fja, 1, [3,1])

print(L)

