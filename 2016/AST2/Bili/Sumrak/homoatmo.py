import numpy as np
import matplotlib.pyplot as plt
import math

#n = 100
#p = 10
#q = 10
A = []
B = []
Ma = 5.15e18 #masa atmosfere
Ha = 11e3 #visina atmosfere
Rz = 6378.1e3 #Poluprecnik Zemlje
PN = 0.78084 #maseni procenat azota
MN = 28.02e-3 #Molarna masa azota
Na = 6.02e23 #Avogadrov broj
sigma = 33.4e-32 #poprecni presek za 589.6 nm azot [m2]
Lambda = 589.6e-9 #[m] azot
ro_atm = 1.225 #gustina atmosfere na 0m, 15oC
ro_n = PN*ro_atm
konc_n = (ro_atm/MN)*Na

"""def Kros(l):
    k = (KrosN*((Ref(LamN)**2 - 1)/(Ref(LamN)**2 + 2))**2/(LamN**4))*((Ref(LamN)**2 - 1)/(Ref(LamN)**2 + 2))**2 / l**4
    return k"""

"""def Ref(l):
    n = 1 + 6.8552e-5 + (3.243157e-2)/(144 - l**(-2))
    return n"""

"""def Konc(m, h, r, P):
    V = 4/3 * np.pi * ((r+h)**3 - r**3)
    n = Na*m*PN/MN
    n = n/V
    return n"""
#n = Konc(Ma, Ha, Rz, PN)
#print(n)
x = 18000*np.random.rand()
y = 18000*np.random.rand()
i = 0
#teta = 2*np.pi*np.random.rand()
teta=5*np.pi/3

while ((y>0) and (y<18000)):
    A.append(x)
    B.append(y)    
    i += 1
    teta = 2*np.pi*np.random.rand()
    #print(teta)
    ksi = np.random.rand()
    tau = -np.log(1-ksi)
    s = tau/(konc_n*sigma)
    print(s)
    x += s*np.cos(teta)
    y += s*np.sin(teta)
teta_ulazno = teta % np.pi    
#print(Konc(Ma, Ha, Rz, PN),teta_ulazno)
plt.scatter(A,B)
plt.show()
#plt.axvline(x = p, color = 'red')
#plt.axhline(y = q, color = 'red')
#plt.axvline(x = 0, color = 'red')
#plt.axhline(y = 0, color = 'red')
