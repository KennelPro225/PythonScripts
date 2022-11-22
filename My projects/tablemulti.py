def table7():
    """fonction qui affiche la table de 7"""
    n =1
    while n< 11:
        print(str(n)+" * 7 = "+str(n*7))
        #print(n*7,end=" ")
        n=n+1


def table(base):
    """fonction qui affiche la table de 'base' passer en parametre"""
    n =1
    print("===> Table de multiplicaation de "+str(base)+"\n")
    while n< 11:
        #print(n*base,end=" ")
        print(str(n)+" * "+str(base)+" = "+str(n*7))
        n=n+1
    print("\n")


def tableMulti(base,debut,fin):
    """fonction qui affiche la table de 'base' passer en parametre"""
    n =debut
    print("===> Table de multiplicaation de "+str(base)+" de "+str(debut)+" à "+str(fin)+"\n")
    while n<= fin:
        #print(n*base,end=" ")
        print(str(n)+" * "+str(base)+" = "+str(n*7))
        n=n+1
    print("\n")
