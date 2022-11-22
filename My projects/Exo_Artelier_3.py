
print("Bienvenue, sur notre programme.")
b= 1+1

print("Veuillez saisir un nombre")
while True:
    
    try:
        num = int(input())
        break
    except:
        print("Vous avez entré une mauvaise valeur: Un entier est réquis")
        print("Veuillez ressaisir un entier:")
   
if num < 0:
    print("Le nombre saisi, est négatif")

elif num > 0:
    print('Le nombre saisi, est positif')

else:
    print("Vous avez saisi 0 et c'est Nul.")
