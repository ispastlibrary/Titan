import numpy as np
x = [0.3, 0.9, 3, 0.11, 0.23, 50, 16]
max = x[0]
min = x[0]
for i in range(len(x)):
    if x[i] > max:
        max = x[i]
        maxi = i
    elif x[i] < min: 
        min = x[i]
        mini = i
        #lista[0]=min
        #x.pop(mini)
#print(x)  
#print('Maksimum je: ', max)
#print('Indeks maksimuma je: ', maxi)
#print('Minimum je: ', min)
#print('Indeks minimuma je: ', mini)

    
 #KAKKO ZAPRAVO SORTIRAS ZA 0.3 sec 
x = np.sort(x, kind='mergesort')

