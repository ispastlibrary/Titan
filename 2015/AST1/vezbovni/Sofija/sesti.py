import numpy as np

L1 = []
for i in range(0,101,2):
    L1.append(i) 
L2 = []
for i in range(1,101,2):
    L2.append(i)
L3 = [L1+L2]
print(L1,L2,L3)