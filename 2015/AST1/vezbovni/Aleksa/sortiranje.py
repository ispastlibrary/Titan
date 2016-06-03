import numpy as np
l, t2 = loadtxt('podaci.txt', unpack = True)

x = [2, 4, 5, 8, 77, 54, 0.1, 0.2]

x=np.sort(x, kind='mergesort')
asd=sum(x)
print(asd)
