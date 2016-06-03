
def temperaturac(a):
    T = 9/5 * a + 32
    print('Temperatura od', a, 'celzijusa je: ', T, 'farenhajta.')
    return T

def temperaturaf(a):
    T= (a - 32) * 5/9
    print('Temperatura od', a, 'farenhajta je: ', T, 'celzijusa.')
    return T

prvat = temperaturac(100)


drugat = temperaturaf(212)

