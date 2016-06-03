import numpy as np

a, l, i ,e, v = np.loadtxt("asteroidi.dat", unpack = True)
n = 0

for j in range(len(a)):
    if (15<i[j])and(i[j]<70)and (v[j]>2.3):
        n+=1
print(n)   
