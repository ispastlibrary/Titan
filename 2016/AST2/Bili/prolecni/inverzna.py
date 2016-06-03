import pylab as pl
import numpy as np

def mul_mat(X,Y):
    Z=np.empty([2,1])
    for i in range(0,2): #rows of A
        for j in range(0,1): #columns of B
            for k in range(0,2): #columns of A and rows of B
                Z[i,j]+=X[i,k]*Y[k,j]
    return Z

def trans_mat(A):
    At=np.empty([2,2])
    for i in range(0,2):
        for j in range(0,2):
            At[i,j]=A[j,i]
    return At

def adj_mat(A):
    A=trans_mat(A)
    for i in range(0,2):
        for j in range(0,2):
            Aadj[i,j]=np.linalg.det(A[i,j])
    return Aadj
A=np.matrix([[2,3],[10,16]])
B=np.matrix([[1],[2]])

det=np.linalg.det(A)
A1=adj_mat(A)
print(mul_mat(A1,B))

