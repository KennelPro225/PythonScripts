depart = 0
fin = 19
be = 0
while depart < fin:
    print("Veuillez entrer un nombre")
    num = int(input())
    a = num
    
    depart +=1
    if be < a:
        be = a
    elif be > a:
        a = be
if be > a:
    print('Le plus grand est:{}'.format(be))
else:
    print("Le plus grand est:{}".format(a))


