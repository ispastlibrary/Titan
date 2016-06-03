niz = [1, 4, 3, 2, 6, 5]
for i in range (len(niz)):
    for j in range(i,len(niz)):
        if niz[i] > niz[j]:
            pom = niz[i] 
            niz[i] = niz[j]
            niz[j] = pom
print(niz)
