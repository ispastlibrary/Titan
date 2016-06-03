x = [0.3, 0.9, 3, 0.11, 0.23, 50, 16]
najm = x[0]
najv = x[0]
for i in range (len(x)):    
    if najm < x[i]:
        najm = x[i]
for i in range(len(x)):
    if najv < x[i]:
        xnajv = x[i]
print(najm)
print(najv)

