import numpy as np
import math
import pylab as pl

R = 1
Unutra = 0
L = [250, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
X = []
Y = []
Y1 = []
A = []
B = []
C = []
D = []

for j in range(0,8):
    for k in range(0,20):
        Unutra = 0
        for i in range(L[j]):
            x=np.random.random()
            y=np.random.random()
            d=math.sqrt(x**2+y**2)
            if (d<=R):
                Unutra+=1   
        odnos = Unutra/(i+1)
        X.append(L[j])
        Y.append(odnos*4)

for i in range(0,len(L)):
    Y1.append(np.pi) 
pl.plot(L,Y1,'orange')
for i in range(0, len(Y)):
    if (Y[i]>=np.pi):
        A.append(Y[i])
        C.append(X[i])
    else:
        B.append(Y[i])
        D.append(X[i])
pl.scatter(C,A,color='purple')
pl.scatter(D,B,color='yellow')
pl.title("Monte Karlo simulacija za izračunavanje broja pi")
pl.xlabel("Broj tačaka")
pl.ylabel("Broj pi") 
pl.show()
