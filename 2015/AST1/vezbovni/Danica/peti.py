def f(n):
    i=n    
    for i in range(n+1, 0, -1):
        if i==1 or i==0:
            return 1
        else:
            return f(i-1)+f(i-2)
               
print(f(5))  

def f1(n):
    if n == 1 or n == 2:
        return 1
    return f1(n-1)+f1(n-2)        
 
print(f1(8))
     
        
'''obrati paznju na white space
stvar je u tome da se po pravilu koriste
4 razmaka, a ne tab. Zato sto program tab razume kao
/t'''

#funkcija f1 je dobra i radi
#stvar sa for petljama je da se i menja prilikom svakog prolaza
#problem nastaje kada ti kazes da ti je i = trazenom broju (n)
#i posle u pitalici uporedjujes sa novim i koje u svakom prolazu sve vise i vise raste
#tako da nikada nece konvergirati ka ovom i==1 i i==0 
