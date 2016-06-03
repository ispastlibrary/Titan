import matplotlib.pyplot as plt
import numpy as np
from  scipy.interpolate import interp1d

fajl1 = input('Unesi ime fajla1:')
fajl2 = input('Unesi ime fajla2:')

r1, i1 = np.loadtxt(fajl1, unpack=True, delimiter=' ')
r2, i2 = np.loadtxt(fajl2, unpack=True, delimiter=' ')

r =abs (r2 - r1)
i = abs(i2 - i1)
gr=30
#print(r)
for j in range(1,32**3):
    if r[j] > gr or i[j]> gr :
        print(j)

