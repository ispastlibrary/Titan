x=[0.3, 9, 11, 3, 1, 50]
def sortirano(x):
    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            return 0
    return 1
while sortirano(x) == 0:
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            t = x[i]
            x[i] = x[i+1]
            x[i+1] = t
print(x)

