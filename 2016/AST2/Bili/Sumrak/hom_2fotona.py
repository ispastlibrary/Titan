import numpy as np
import matplotlib.pyplot as plt
import math

PN = 0.78084 #maseni procenat azota
MN = 28.02e-3 #Molarna masa azota
Na = 6.02e23 #Avogadrov broj
sigma = 33.4e-32 #poprecni presek za 589.6 nm azot [m2]
Lambda = 589.6e-9 #[m] azot
ro_atm = 1.225 #gustina atmosfere na 0m, 15oC
ro_n = PN*ro_atm
konc_n = (ro_atm/MN)*Na

A1 = []
B1 = []
A2 = []
B2 = []


x1 = 1000000*np.random.rand()
y1 = 1000000*np.random.rand()
x2 = 1000000*np.random.rand()
y2 = 1000000*np.random.rand()
teta1 = 2*np.pi*np.random.rand()
teta2 = 2*np.pi*np.random.rand()

i = 0
while ((y1>0) and (y1<1000000)):
    A1.append(x1)
    B1.append(y1)    
    i += 1
    teta1 = 2*np.pi*np.random.rand()
    ksi = np.random.rand()
    tau = -np.log(1-ksi)
    s = tau/(konc_n*sigma)
    x1 += s*np.cos(teta1)
    y1 += s*np.sin(teta1)
i = 0
while ((y2>0) and (y2<1000000)):
    A2.append(x2)
    B2.append(y2)    
    i += 1
    teta2 = 2*np.pi*np.random.rand()
    ksi = np.random.rand()
    tau = -np.log(1-ksi)
    s = tau/(konc_n*sigma)
    x2 += s*np.cos(teta2)
    y2 += s*np.sin(teta2)

teta_ulazno1 = teta1 % np.pi    
teta_ulazno2 = teta2 % np.pi
#plt.figure(1)
#plt.subplot(211)
plt.scatter(A1, B1, color = 'FFBAD2')
#plt.subplot(212)
plt.scatter(A2, B2, color = "green")
plt.scatter()
plt.show()