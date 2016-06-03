


def FibonacijevNiz(N):
    if N==1:
   	 return 1
    elif N==2:
   	 return 1
    else:  
        #print(FibonacijevNiz(N-1) + FibonacijevNiz(N-2))
        return(FibonacijevNiz(N-1) + FibonacijevNiz(N-2))
    

x=FibonacijevNiz(6)
print(x)
