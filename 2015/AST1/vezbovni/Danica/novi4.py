x=[1,7,0,5,6,3,2,111]

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
             pom=x[i]
             x[i]=x[j]
             x[j]=pom
 
print(x)



