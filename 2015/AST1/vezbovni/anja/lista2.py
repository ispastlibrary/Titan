import numpy as np
x=[0.3, 0.9, 3.0, 0.11, 0.23, 50, 16]
maxelem=x[0]
minelem=x[0]
for i in range(len(x)):
    if maxelem< x[i]:
        maxelem= x[i]
    if minelem> x[i]:
        minelem= x[i]

print ("najveci clan je: ", maxelem)
print ("najmanji caln je: ", minelem)

x=np.sort(x, kind='mergesort')

    
