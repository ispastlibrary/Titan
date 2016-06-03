lista = ['jan', 3, 'mart', 3.14]
print(lista[1])
print (len(lista[0])
# ovo nam vraca duzinu liste/clana

lista1=np.array[1,2,3,4]
lista2=np.array[7.8.9.4]

lista3=lista1+lista2

for i in lista:
    print(i)
#vraca clan po clan funkcije
for i in range(len(lista)):
    print(lista[i])


for i in range(len(lista)):
    print(i)

lista.pop()
print(lista)
#izbacuje poslednji clan

lista.insert(1, 'asd')
print (lista)
#ovo prvi clan pretvrara u asd i pomera ostale u desno
import numpy as np

start = 0
stop = 10
korak= 0.1
x=np.arange(start, stop, korak)
#sve clanove od 0 do 10 za 0.1
print(x)

np.sin(np.pi/2)
np.cos(2)
np.exp(1)

np.log(32)# ovo je log na osnovu e od 32
np.log10(32)# ovo je log na osnovu 10 od 32

lista = [1,2,3,4,5,6]

def fun(x):
    return x[0]
print(fun(lista))

