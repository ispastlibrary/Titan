import numpy as np
import matplotlib.pyplot as plt 

S = 1
I1 = 5
c = 3e8
v0 = 3.0/656 * 10**17
vd = np.sqrt(2 * 1.38 * 10**-23 * 10000/(1.7 * 10**-27) ) * v0 / c 
v = np.linspace(-5 * vd + v0, v0 + 5 * vd, num = 200)
Dp = 1/(np.sqrt(3.14)*vd) * np.exp(-((v - v0)/vd)**2)
x = (v -v0) * 10**-14

T = 10**10 * Dp
u= np.arange(0, 1.2, 0.2)
I = np.linspace(0, 0, 6)

def limb(u):
    I = S + np.exp(-T/u)*(I1-S)
    return I

#for i in range(len(u)):
   # if i == 0:
    #    I[0] = S
   # else:
     #   y = limb(u[i])
    #    I[i] = min(y)

#print (u)
#print (I)

#plt.plot(u,I, '-g', label = "Jedan mnogo kul grafik")

plt.plot(x, limb(1), '-b' )
plt.plot(x, limb(0.5) , '-g')
plt.show()
