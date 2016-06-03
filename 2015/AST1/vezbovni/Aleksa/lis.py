x=[0.3, 100, 0.77, 23, 0.2, 50, 16]

y=x[0]

for i in range(len(x)):
    if x[i] > y:
       y = x[i] 
    else:
        y = y
print (y)
    
z=x[0]

for i in range(len(x)):
    if x[i] < z:
       z = x[i]
    else:
        z = z
print(z)       
