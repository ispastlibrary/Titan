import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

T, l, dl = np.loadtxt('merenja3.txt', unpack = True)

def funkcija(x, a, b, c):
    return a*x**2+b*x+c

parametri, cov_m = curve_fit(funkcija, T, l, sigma= dl)

greske_parametara=np.sqrt(np.diag(cov_m))

print('Parametar a je: ', parametri[0], '+/-', greske_parametara[0])
print('Parametar b je: ', parametri[1], '+/-', greske_parametara[1])
print('Parametar c je: ', parametri[2], '+/-', greske_parametara[2])



