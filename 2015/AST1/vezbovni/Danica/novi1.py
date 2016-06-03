import numpy as np
lista=[1,2,3,4,5,6,7]

def fun(x):
    return x[0]

print(fun(lista))


for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

for i in range(len(lista)):
    print(i)

lista.pop()
print(lista)

lista.insert(1, 'asd')
print(lista)


start=0
stop=10
korak=0.1
x=np.arange(start, stop, korak)

print(x)

np.sin(2)

np.cos(2)

np.exp(1)

np.sin(np.pi/2)

np.log(32)

np.log10(32)

