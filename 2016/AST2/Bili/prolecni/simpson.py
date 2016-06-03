import pylab as pl
import math
import numpy as np

file=np.loadtxt("NUM_PS_2_Podaci.txt")
L = file[:,0]
I = file[:,1]

#print(L[len(L)-1])
a = 0
b = len(L)-1
h = L[1]-L[0]

def Simp_all(a,b,h):
    Odd = 0
    Even= 0
    for i in range(a+1,len(L)-1):
         if (i%2==0):
              Even+=I[i]
         else:
              Odd+=I[i]
    area=h/3*(I[a]+2*Even+4*Odd+I[b])
    return area

print((L[b]-L[a])-Simp_all(a,b,h))
