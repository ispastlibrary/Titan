import matplotlib.pyplot as plt
import numpy as np


a = np.arange(-21, 21) 
rezultat = [] 

def funkcija(x):
    y = x**2
    return y

for i in range(len(a)):
    h = funkcija(a[i])
    rezultat.append(h)
    print(h)
print(rezultat)

plt.scatter(a, rezultat)
plt.plot(a, rezultat)
plt.show()
#x = 2
#u = funkcija(x)
#print(u)
