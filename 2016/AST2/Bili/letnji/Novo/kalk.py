import numpy as np

tau = 1/(5.6e-6+2e-15*1.5e8) #Natrijum
tau1 = 1/(7e-8+2e-15*1.5e8) #Vodonik
tau2 = 1/(1e-3+1.59e-17*1.5e8) #Voda
rez = (tau2/((0.6)**2))
print(tau)
print(tau1)
print(tau2)
print(rez)
