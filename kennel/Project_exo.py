"""
#Programme: "Jeu du juste prix" qui consiste à demander au joueur d'entrer le bon prix 
			et si le prix est moins le programme le notifie et lui donne une chance infinie dans le 
			mode facile. Par contre, dans le mode difficile, il a 10 chances de reussir 
			sinon le jeu est perdu 

#Email: kennelkassi@gmail.com

#Auteur: Kassi G. Kennel Programmeur Junior en Python
"""

import random
from time import sleep
from sys import exit
a =[1000,1250,1500,1750,2000,2250,2500,2750,3000,3250,3500,3750,4000,4250,4500,4750,5000,5250,5500,5750,6000,6250,6500,6750,7000,7250,7500,7750,8000,8250,8500,8750,9000,9250,9500,9750,10000]
x = random.choice(a)
n = 1
y = random.choice(a)
random.shuffle(a)


print("***CONDITION***\n Le jeu du Juste prix va consister à trouver le prix exact que le programme va générer.\nSi le prix saisi est exact vous, aurez une proposition à passer au mode difficile\n\nNB:Le prix se trouve entre 1000 & 10000 avec un surplus de 250 pour vous aider\nExemple: 1000-1250-1500-...5250-...")
sleep(5)
print("\nTrouve le juste prix")
quest = int(input())


while quest != x:
    if quest < x:
        print("c’est moins, veillez réessayer")
        quest = int(input())
    elif quest > x:
        print("c’est plus, veillez réessayer")
        quest = int(input())

if x == quest:
    print("Vous avez trouvé le juste prix")


print("Voulez-vous continuer? 1- Oui 0- Non")

answer2 = int(input())
if answer2 == 1:
	
	print("Vous êtes dans le Mode difficile")
	print("Devinez, le juste prix")
	request2 = input()
	while request2 != y and n < 10:
		print("Mauvaise réponse, veuillez réessayer!")
		print("Il vous reste,", 10-n,"chances")
		request2 = input()
		n+=1
else:
	if answer2 == 0:
		exit()

if request2 == y:
	print("Vous avez trouvé le juste prix")
else:
	print("Vous avez perdu le jeu!")










    
    
