lista = [2,98,867,56,5,1,4,3,760]

najmanji = lista[0]
najveci = lista[0]

for i in range(len(lista)):
    if lista[i] < najmanji:
        najmanji = lista[i]
    if lista[i] > najveci:
        najveci = lista[i]

print(najmanji)
print(najveci)
