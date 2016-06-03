x = [0.3, 0.9, 3, 0.11, 0.23, 50, 16]
najmanji = x[0]
najveci = x[0]
for i in range(len(x)):
    if najmanji > x[i]:
        najmanji = x[i]
    if najveci < x[i]:
        najveci = x[i]

print(najmanji)
print(najveci)
