x=[1,2,3,4,5,6,7] 

i=0
while (i<=len(x)-1):
    if i%2==0:
        for j in range(i+1, len(x)):
            x[i]=x[j]
            x.pop()
        

print(x)


