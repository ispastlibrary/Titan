import numpy as np

L1 = []
for i in range(0,101,2):
    L1.append(i)

L2 = []

for x in range(1,101,2):
    L2.append(x)

L3 = []
L3.extend(L1+L2) #odlicno resenje problema 

print(L1, L2, L3)

L3=np.sort(L3, kind='merge-sort') #ovako sortiras listu
print(L3)
