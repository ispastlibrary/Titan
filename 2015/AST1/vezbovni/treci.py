def povrs(a, b):
    P = a*b
    print("povrsina je: ", P)
    return P


prvi = povrs(3, 5)
drugi = povrs(4, 10)

def obim(a, b):
    O = 2*a + 2*b
    print("O je:", O)
    return O


prvi = obim(3, 5)
drugi = obim(4, 10)

#def temp(C, F):

def f2c(x):
    t_c=(x-32)*(5/9)
    print('temp je: ', t_c)
    return t_c 

temp=f2c(104)


def c2f(x):
    t_f=(9/5)*x+32
    print('temp je: ', t_f)
    return t_f

temp=c2f(100)
