number = 7
guess = -1
 
print("Pogodite broj!")
while guess != number:
    guess = int(input("Da li je... "))
 
    if guess == number:
        print("Bravo! Pogodili ste!")
    elif guess < number:
        print("Broj je veci od toga...")
    elif guess > number:
        print("Broj nije toliko veliki.")
