x = [0.3, 0.9, 3, 0.11, 0.23, 50, 16]
y = []
#min = x[0]


while len(x) > 0:
    min=x[0]
    for i in range(len(x)):
        if min > x[i]:
            min=x[i]
    y.append(min)
    x.remove(min)

print(y)
print(x)
