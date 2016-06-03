print('Unesite koji po redu broj fibonacijevog niza zelite da prikazete na ekranu.')
a = int(input())
j=1
d=1
for c in range(a-2):
    t=j+d
    j=d
    d=t
   
print('Trazeni broj je ', t, '. Hvala sto ste koristili nas program.')
    
    

