#lista = ['jan', 3, 'mart', 3.14]
#print(lista[1])
#print(len(lista))

#len(lista)  nam vraca duzninu list

#lista1=np.array ([1.2.3.4])
#lista2=np.array([5.6.7,9])

#lista3=lista1+lista2
#print(lista3) 
#ovo nam spaja dve liste, za vektore np.array, za ostalo bez

for i in lista:
    print(i)
#vraca clanove

for i in range(len(lista)):
    print(i)
#vraca indekse

for i in range(len(lista)):
    print(lista[i])
#vraca clanove

lista.pop()
print(lista)
#izbacuje poslednji clan

lista.insert(1, 'asd')
print(lista)
#na mesto clana sa indeksom 1 ubaci asd,a strai 1 se pomeri za jedno mesto desno


import numpy as np
lista= [ 'jan', 3, 'mart, 3.14]
def fun(x):
    return x[0]
start= 0
stop = 10
korak = 0.1
x=np,arrange(start, stop, koran)
print(x)

np.sin(np.pi/2)
np.cos(2)
pr.exp(1)
#np-biblioteka

np. log(32) #osnova e
np.log10(32) #osnova 10
np.log2(42) #osnova 2
 
