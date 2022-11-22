"""
#Programme: "Jeu du juste prix" qui consiste à demander au joueur d'entrer le bon prix 
			 et si le prix est moins le programme le notifie et lui donne une chance infinie dans le 
			 mode facile. Par contre, dans le mode difficile, il a 10 chances de reussir 
			 sinon le jeu est perdu 

#Email: kennelkassi@gmail.com

#Auteur: Kassi G. Kennel Programmeur Junior en Python
"""

import random
import os
from time import sleep
from sys import exit

def game_attempt1():
    print("c’est moins, veillez réessayer")
def game_attempt2():
	print("c’est plus, veillez réessayer")
def score_win():
    global nom
    global score
    x = nom + "\n"
    
    
    os.chdir("c:\\Jeu du Juste Prix")
    c = open("Data.txt","a+")
    b = c.write(x)
   
    

"""
 cette boucle est pour rendre ce jeu infini je vais essayer de trouver un moyen qui va permettre a l'utilisateur de pouvoir 
 revenir en arrière(sortir de la boucle) s'il le veut vraiment  après confirmation
 """   
    


running = True
while running:
    a =[1000,1250,1500,1750,2000,2250,2500,2750,3000,3250,3500,3750,4000,4250,4500,4750,5000,5250,5500,5750,6000,6250,6500,6750,7000,7250,7500,7750,8000,8250,8500,8750,9000,9250,9500,9750,10000]
    x = random.choice(a)
    n = 1
    y = random.choice(a)
    p = random.choice(a)
    g = random.choice(a)
    score = 0
    
    print("Veuillez entrer votre nom!")
    nom = input()
    score_win()

    """
    Pour raccourcir le programme j'ai utilisé la liste nommé 'a' pour pouvoir saisir les valeurs avec un ecart de 250
    partant de 1000 à 10000.
    Importer le module random et la fonction choice a deux reprise pour rendre encore plus difficile le jeu
    la variable qui contient le premier choix est la variable 'x' elle est contient le prix de la partie facile
    et 'y' est celle qui contient celle de la partie difficile.
    """
    print("***CONDITION***\n Le jeu du Juste prix va consister à trouver le prix exact que le programme va générer.\nSi le prix saisi est exact vous, aurez une proposition à passer au mode difficile\n\nNB:Le prix se trouve entre 1000 & 10000 avec un surplus de 250 pour vous aider\nExemple: 1000-1250-1500-...5250-...")
    sleep(5)
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
            score += 1
            score_win()
            
    print("\nTrouve le juste prix")
    quest1 = int(input())
    #Quest est la variable permettant à l'utilisateur d'entrer des valeurs via son interface, qui sont directement convertis en entier
    while quest1 != p:
        if quest1 < p:
            game_attempt1()
            quest1 = int(input())
            
        elif quest1 > p:
            game_attempt2()
            quest1 = int(input())
    #Cette boucle est faite pour redonner la chance à l'utilisateur à donner une autre valeur, et elle permet que le mode facile soit infini
        if p == quest1:
            print("\nVous avez trouvé le juste prix")
            score += 1
            score_win(nom,score)
    
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
            score_win(nom,score)
            exit()

    if request2 == y:
        print("Vous avez trouvé le juste prix")
        score += 10
        score_win()
    else:
        print("Vous avez perdu le jeu!")
        score_win(nom,score)
    
    print("\nDevinez, le juste prix")
    request3 = int(input())
    while request2 != g and n < 10:
        print("Mauvaise réponse, veuillez réessayer!")
        print("Il vous reste,", 10-n,"chances")
        request3 = int(input())
        n+=1
        if request3 < g:
            game_attempt1()
        else:
            if request3 > g:
                game_attempt2()
    if request3 == g:
        print("Vous avez trouvé le juste prix")
        score += 10
        score()
    else:
        print("Vous avez perdu le jeu!")
        a = score_win()