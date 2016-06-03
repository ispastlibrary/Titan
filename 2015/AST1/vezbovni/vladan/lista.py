import numpy as np

L1 = []
L2 = []

for i in range(1,101):
    if i%2 == 0:
        L1.append(i)
    else:
        L2.append(i)

L1.extend(L2)

L3 = np.sort(L1)

for i in range(len(L3)):
    print(L3[i])

