x = [0.3, 0.9, 0.11, 0.23, 50, 16]
y = x[0]
for i in range(len(x)-1):
    if y>x[i+1]:
        y = x[i+1]
print(y)
