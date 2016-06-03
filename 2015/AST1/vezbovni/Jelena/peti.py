def faktorijel(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * faktorijel(n-1)

print(faktorijel(3))
