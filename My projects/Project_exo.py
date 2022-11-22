"""
#Programme: "Jeu du juste prix" qui consiste à demander au joueur d'entrer le bon prix 
			 et si le prix est moins le programme le notifie et lui donne une chance infinie dans le 
			 mode facile. Par contre, dans le mode difficile, il a 10 chances de reussir 
			 sinon le jeu est perdu 

#Email: kennelkassi@gmail.com

#Auteur: Kassi G. Kennel Programmeur Junior en Python
"""

import random

from sys import exit

def game_attempt1():
    print("c’est moins, veillez réessayer")
def game_attempt2():
	print("c’est plus, veillez réessayer")


a = range(1000,10001 )
x = random.choice(a)
n = 0
y = random.choice(a)

"""
Pour raccourcir le programme j'ai utilisé la liste nommé 'a' pour pouvoir saisir les valeurs avec un ecart de 250
partant de 1000 à 10000.
Importer le module random et la fonction choice a deux reprise pour rendre encore plus difficile le jeu
la variable qui contient le premier choix est la variable 'x' elle est contient le prix de la partie facile
et 'y' est celle qui contient celle de la partie difficile.
"""

print("***CONDITION***\n Le jeu du Juste prix va consister à trouver le prix exact que le programme va générer.\nSi le prix saisi est exact vous, aurez une proposition à passer au mode difficile\n\nNB:Le prix se trouve entre 1000 & 10000 avec un surplus de 250 pour vous aider\nExemple: 1000-1250-1500-...5250-...")

print("\nTrouve le juste prix")
quest = int(input())
#Quest est la variable permettant à l'utilisateur d'entrer des valeurs via son interface, qui sont directement convertis en entier

while quest != x:
    if quest < x:
        game_attempt1()
        quest = int(input())
    elif quest > x:
        game_attempt2()
        quest = int(input())
#Cette boucle est faite pour redonner la chance à l'utilisateur à donner une autre valeur, et elle permet que le mode facile soit infini
if x == quest:
    print("\nVous avez trouvé le juste prix")


print("Voulez-vous continuer? 1- Oui 0- Non")

answer2 = int(input())
if answer2 == 1:
	
	print("Vous êtes dans le Mode difficile")
	print("\nDevinez, le juste prix")
	request2 = int(input())
	while request2 != y and n < 10:
		print("Mauvaise réponse, veuillez réessayer!")
		print("Il vous reste,", 10-n,"chances")
		request2 = int(input())
		n+=1
		if request2 < y:
			game_attempt1()
		else:
			if request2 > y:
				game_attempt2()
#Cette condition if et cette boucle, font le choix et 
else:
	if answer2 == 0:
		exit()

if request2 == y:
	print("Vous avez trouvé le juste prix")
else:
	print("Vous avez perdu le jeu!")
