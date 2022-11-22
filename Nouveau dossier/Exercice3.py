from random import choice

n = choice(range(0,101))
print(n)

while True:
    saisie = int(input("Veuillez saisir un entier:\t"))
    if saisie > n:
        print("PLUS PETIT")
    elif n > saisie:
        print("PLUS GRAND")
    else:
        if saisie == n:
            print("Bravo")
            break
