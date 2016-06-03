a = [1,3,5,2,7,4,0, 0]
for m in range(len(a)):    
    for n in range(m,len(a)):
        if(a[m] > a[n]):
            pom=a[m]; a[m]=a[n]; a[n]=pom
print(a)
         
     
