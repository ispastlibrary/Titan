lista=[0, 2, 7, 9, 22, 34, 51, 86, 12]
i = 0
n = len(lista)
j = 0
lista1 = []
for i in range(len(lista)):
    if i%2 == 0:
        lista1.insert(j, lista[i])
        j+=1
 


#lista.remove(vrednost)
print(lista)
