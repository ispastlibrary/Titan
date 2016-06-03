def fib(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)

#print(fib(18))
#print(fib(19))
#print(fib(20))
#print(fib(21))

def fibn(n):
    tek=1
    preth=0
    for i in range(1,n+1):
        p=tek
        tek+=preth
        preth=p
        print(p)

fibn(20)
