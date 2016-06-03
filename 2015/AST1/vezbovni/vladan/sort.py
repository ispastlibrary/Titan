import numpy as np

x = [34, 13, -5, 16, -32, 9]
print(x)

niz = np.array(x)

def minniz(x, poc):
    m = poc
    for i in range(x+1, len(x)):
        if x[m] > x[i]:
            m = i
    return m

for i in range(len(niz) - 1):
    p = niz[i]
    k = minniz(niz, i+1)
    niz[i] = niz[k]
    niz[k] = p
    

print(niz)
