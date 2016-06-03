x = [1, 2.14, 0.14, 152]
y =x[0]
for i in range(len(x)-1):
    if y<x[i+1]:
        y = x[i+1]
print(y)
