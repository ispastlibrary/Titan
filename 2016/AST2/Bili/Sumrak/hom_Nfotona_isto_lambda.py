import numpy as np
import matplotlib.pyplot as plt

PN = 0.78084 #maseni procenat azota
MN = 28.02e-3 #Molarna masa azota
Na = 6.02e23 #Avogadrov broj
Lambda = 450 #[nm] azot
sigma = 33.4e-32*(589.6/Lambda)**4 #poprecni presek u zavisnosti od talasne duzine za azot [m2]
ro_atm = 1.225 #gustina atmosfere na 0m, 15oC [kg/m3]
ro_n = PN*ro_atm
konc_n = (ro_atm/MN)*Na

N = 100 #broj fotona 
A = []
B = []
x = np.zeros(N)
y = np.zeros(N)
a = 18000*np.random.rand()
b = 18000
for i in range(N):
    x[i] = a
    y[i] = b
    teta = 5*np.pi/3
    j = -1
    while ((y[i] > 0) and (y[i] <= 18000)):
        A.append(x[i])
        B.append(y[i])        
        ksi = np.random.rand()
        tau = -np.log(1-ksi)
        s = tau/(konc_n*sigma)
        x[i] += s*np.cos(teta)
        y[i] += s*np.sin(teta)
        teta1 = teta
        teta = 2*np.pi*np.random.rand()
        j += 1
    teta_pada = teta1 % np.pi
    x[i] = x[i]-y[i]/np.tan(teta_pada)
    print("redni broj fotona:",i,"raseje se",j,"puta","nalazi se na x osi:",x[i],"upadni ugao:", teta_pada)    
plt.scatter(A,B)
plt.show()