print("Combien de nombre, voulez vous saisir?")
fois = int(input())
be = 0
d = 0
e = 0
liste = []
listeposi = []
listenega = []
c = len(liste)
while c < fois:
    print("Veuillez saisir un nombre svp!!")
    num  = int(input())

    a = num
    liste.append(a)
    fois -= 1

    
    
f = len(liste)  
    
while be < f:
    if liste[be]>d:
        liste[be] = d
        listeposi.append(d)
    else:
        if liste[be] < e:
            liste[be] = e
            listenega.append(e)
    be +=1

    

print('\n',liste,'\t',listeposi,'\t',listenega)


