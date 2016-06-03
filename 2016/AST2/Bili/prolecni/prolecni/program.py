import numpy as np
import matplotlib.pyplot as plt

x, y, dy = np.loadtxt("barometarska.txt" , unpack=True)

N = len(x)

def Min(y, fun, dy):
    min = ((y - fun)**2)/(2*dy**2)
    return min

def Fun(a, b, x):
    fun = a*np.exp(-b*x)
    return fun


#a od 1.15 do 1.45
#b od 0.01 do 0.009
ak2 = 1.45
ak1 = 1.15

bk2 = 0.09
bk1 = 0.01

br = 1000

da = (ak2 - ak1)/br
db = (bk2 - bk1)/br
sume = []

a = ak1
b = bk1

for i in range(br):
    for k in range(br):
        sum = 0
        for g in range(N):
            fun = Fun(a, b, x[g])
            sum += Min(y[g], fun, dy[g])
        if (k == 0):
            summin = sum
        if (sum < summin):
            amin = a
            bmin = b
        b += db
    a += da

y1 = []
y1 = Fun(amin, bmin, x)
print(amin, bmin)
plt.plot(x, y1)
plt.scatter(x, y)
plt.show()
