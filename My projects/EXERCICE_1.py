# EXERCICE 1
from random import choice

while True:
    n = int(input("Veuillez entrer un entier:\t"))
    if n < 1:
        n = int(input("Veuillez entrer un entier encore:\t"))
    
    elif n >= 1:
        n_hasard = choice(range(0,n))
        print("Nombre au hasard:{}".format(n_hasard))
        break


