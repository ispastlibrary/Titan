import numpy as np
import matplotlib.pyplot as plt

PN = 0.78084 #maseni procenat azota
MN = 28.02e-3 #Molarna masa azota
Na = 6.02e23 #Avogadrov broj
Lambda = 589.6 #[m] azot
sigma = 33.4e-32*(589.6/Lambda) #poprecni presek za 589.6 nm azot [m2]
ro_atm = 1.225 #gustina atmosfere na 0m, 15oC
ro_n = PN*ro_atm
konc_n = (ro_atm/MN)*Na

parovi = [] 
x = 18000*np.random.rand()
y = 180000
teta = 5*np.pi/3

while ((y>0) and (y <= 180000)):
    parovi.append((x,y)) 
    print(x,y)
    ksi = np.random.rand()
    tau = -np.log(1-ksi)
    s = tau/(konc_n*sigma)
    print(s)
    x += s*np.cos(teta)
    y += s*np.sin(teta)
    teta1 = teta    
    teta = 2*np.pi*np.random.rand()    
teta_ulazno = teta1 % np.pi
dx = y/np.tan(teta_ulazno)
x -= dx  
parovi.append((x,0))   
plt.plot(*zip(*parovi))
plt.show()