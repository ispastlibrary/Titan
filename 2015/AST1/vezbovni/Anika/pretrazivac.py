x=[0.3, 0.9, 3, 0.11, 0.23, 50, 16]

min=x[0]
y=[]

while len(x) > 0:
    min=x[0]
    for i in range(len(x)):
        if  min > x[i]:
            min=x[i]
    x.remove(min)
    y.append(min)

print(y)
#print('max', max)
#print('min', min)


#x.pop([i])
#x.remove(vrednost)

#y=[]
#y.append(asd)

'''
min=x[0]

for i in range(len(x)):
    if x[i]==min:
        n_l.append(x[i])
    sortedx=[]
'''
