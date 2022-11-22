from http.client import TOO_MANY_REQUESTS


list = []
negatif = []
positif = []

debut = 0
fin = 10

while debut < fin:
    while True:
        try:
            saisir = int(input("Veuillez saisir des nombres entiers"))
        except ValueError:
            print("Veuillez résaisir un integer svp!!")
        finally:
            break
    list.append(saisir)

    debut+=1


for i in list:
    if i> 0:
        positif.append(i)
    else:
        negatif.append(i)
print("Les nombres positifs sont:{}".format(positif))
print("Les Nombres negatifs sont:{}".format(negatif))

 