
broj = 42
nebroj = -1
while nebroj != broj:
    nebroj = int(input('Unesite broj: '))
    if nebroj < broj:
        print('Vas broj je manji od trazenog broja. Pokusajte ponovo. Hvala.')
    elif nebroj > broj:
        print('Vas broj je veci od trazenog broja. Pokusajte ponovo. Hvala.')
    else:
        print('Vas broj jeste trazeni broj. Igrajte se ponovo sa nama. Hvala.')
