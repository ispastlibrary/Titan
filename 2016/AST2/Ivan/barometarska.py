import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x,y,err = np.loadtxt("barometarska.txt", unpack=True, delimiter=' ')

def fja(a,b):
    a=1.5
    b=0.05
    return fja=a*2.718**(-b*x)
plt.plot(x,fja)
plt.plot(x,y,'ok')
plt.errorbar(x,y,yerr=err, fmt=None)
plt.show()

