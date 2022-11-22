
from random import choice

while True:
    n = int(input("Veuillez entrer un entier:\t"))
    if n <= 1:
        n = int(input("Veuillez entrer un entier encore:\t"))
    
    else:
        n_hasard = choice(range(0,n))
        tirage_mille = choice(range(0,1001))/n
        tirage_10mille = choice(range(0,10001))/n
        tirage_100mille = choice(range(0,100001))/n
        tirage_million = choice(range(0,1000001))/n
        print("{}\n{}\n{}\n{}".format(tirage_mille,tirage_10mille,tirage_100mille,tirage_million))
        break