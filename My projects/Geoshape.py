def Ptriangle(a,base,c):
    P = a + base+ c
    return P

def Atriangle(base,hauteur):
    A = base*hauteur/2
    return A

def Pcarre(C):
    P = 4*C
    return P

def Acarre(C):
    A =  C**2
    return A

def Prect(base,hauteur):
    P = 2*(base + hauteur)
    return P

def Arect(base,hauteur):
    A = base*hauteur
    return A

def Ppara(a,base):
    P  = 2 * (a+base)
    return P

def Apara(base,hauteur):
    A = base * hauteur
    return A

def Ptrap(b,a,base,c):
    P = b+a+base+c
    return P

def Atrap(b,base,hauteur):
    A =  (b+base)*hauteur/2
    return A

def Ppoly(n,c):
    P = n*c
    return P

def Apoly(c,a,n):
    A = c*a*n/2

def Pcercle(rayon):
    Pi = 3.14
    P = 2*Pi*rayon
    return P

def Acercle(rayon):
    Pi = 3.14
    A = (rayon*Pi)**2
    return A




