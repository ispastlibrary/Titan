import numpy as np
import pylab as pl

def mnozenje(X,Y):
    Z=np.empty([2,1])
    for i in range(0,2):
       for j in range(0,1):
          for k in range(0,2):
              Z[i,j]+=X[i,k]*Y[k,j]
    return Z
def trans(X):
    AT=np.empty([2,2])
    for i in range(0,2):
        for j in range(0,2):
            AT[i,j]=A[j,i]
    return AT

def adjun(X):
    AT=trans(X)
    for i in range(0,2)
    
AT = trans(A)

A = np.matrix([[2,3],[10,16]])
B = np.matrix([[1],[2]])

print(mnozenje(A,B))
