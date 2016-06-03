import numnpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
D , V , dV=np.loadtxt('merenja.txt' , unpack=True)

def fun(a,b):
    return a*b
a=D
b=H
plt.plot(D,V,'-r', label='fitovanje')
plt.errorbar(x,y,yerr=dV, fmt='*')
plt.xlabel('x-osa')
plt.ylabel('y-osa')
plp.title('Grafik zavisnosti brzine od razdaljine)
plt.show()
