"""
Hoću da mi kažeš:

1) Kolika je inklinacija orbite Marsa?
2) Kako se inklinacija menja sa vremenom?
3) Kolika je brzina Marsa u uzlaznom čvoru i perihelu?
4) Koliki je ekscentricitet Marsove orbite?
5) Koliko je rastojanje Marsa u perihelu i afelu?
6) Koliko je vremena potrebno da Mars stigne od uzlaznog čvora do afela?
"""

import numpy as np
import matplotlib.pyplot as plt

t,x,y,z=np.loadtxt("mars.dat", unpack=True, delimiter=',')



plt.plot(t,z)
plt.show()














min=2
max=0
for i in range(len(t)):
    d= (x[i]**2+y[i]**2+z[i]**2)**(1/2)
    if (d<min):
        min=d
    if (d>max):
        max=d
print ("aph", max)
print ("per", min)





