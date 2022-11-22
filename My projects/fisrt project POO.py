class Homme:
    Client = 0
    def __init__(self,age,poids,taille,name,sexe):
        Homme.Client +=1
        self.age = age
        self.poids = poids
        self.taille = taille
        self.name = name
        self.sex = sexe

print("Salut!! Bienvenue sur notre Plateforme de calcul de Masse.\n")

print("Quel est votre Prénon s'il vous plait")
name = input()

print("\nVeuillez saisir votre Ages il vous plaît")
age = int(input())

print("\nVeuillez saisir votre Poids s'il vous plaît en Kg")
poids = int(input())

print("\nVeuillez saisir votre Taille s'il vous plaît en m")
Taille = float(input())




