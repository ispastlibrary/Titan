A = [0]*102
A[0] = 1
A[1] = 1
for i in range(100):
    print(i)
    A[i+2] = A[i+1]+A[i]
    print(A[i+2])

