def fib(k):


    a=1
    b=1
    n=2
    for i in range(k-2):
        n = a + b
        a=b
        b=n
    print (b)
fib (7)

