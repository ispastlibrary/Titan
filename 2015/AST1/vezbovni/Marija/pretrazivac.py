x=[0.2, 3, 0.39, 0.18, 0.23, 0.65, 16, 20]

min = 0.2
max = 0.2

for i in range(len(x)):
    if x[i]<min:
        min = x[i]
        mini = i    
    elif x[i]>max:
        max = x[i]
        maxi= i
print('Indeks minimalnog je', mini)
print ('Indeks maksimalnog je', maxi) 
print('Minimum je', min)
print('Maksimum ja', max)

x.pop()
x.pop(0)

print(x)

x = np.sort(x, kind='mergesort')
