from random import*

print("Veuillez entrer votre pseudo")
name1 = input()
a = ["Graven","Herve","Mark","Jason"]
name2 = choice(a)
running = True

class Player1:
    pseudo = name1
    life = 250
    attack = 2
class Player2:
    pseudo = name2
    life = 250
    attack = 2

partie = 0
print("Joueur 1",Player1.pseudo,"\nJoueur 2,",Player2.pseudo)




ordi = Player2.life
realplayer = Player1.life
#partie 1: Joueur 1 essaye
print("\nCombat 1")
coup1 = choice(range(0,100))
if coup1 != 0:
    print(Player1.pseudo,"a réussi son coup")
    print("\nJoueur 1",Player1.pseudo,realplayer,"/Joueur 2",Player2.pseudo,ordi-coup1)
else:
    print(Player1.pseudo,"a raté son coup.")
input()
#partie 2: Joueur 2 essaye
print("\nCombat 2")
coup2 = choice(range(0,100))
if coup2 != 0:
    print(Player2.pseudo,"a réussi son coup")
    print("\nJoueur 1",Player1.pseudo,realplayer-coup2,"/Joueur 2",Player2.pseudo,ordi-coup1)
else:
    print(Player2.pseudo,"a raté son coup.")
input()
#partie 3: Joueur 1 essaye
print("\nCombat 3")
coup3 = choice(range(0,100))
if coup3 != 0:
    print(Player1.pseudo,"a réussi son coup")
    print("\nJoueur 1",Player1.pseudo,realplayer - coup2,"/Joueur 2",Player2.pseudo,ordi-(coup3+coup2))
else:
    print(Player1.pseudo,"a raté son coup.")
input()
#partie 4: Joueur 2 essaye
print("\nCombat 4")
coup4 = choice(range(0,100))
if coup4 != 0:
    print(Player2.pseudo,"a réussi son coup")
    print("\nJoueur 1",Player1.pseudo,realplayer-(coup2+coup4),"/Joueur 2",Player2.pseudo,ordi-(coup1+coup3))
else:
    print(Player2.pseudo,"a raté son coup.")
    
    
if realplayer-(coup4+coup2) < ordi-(coup1+coup3):
    print("\n\n",Player2.pseudo, "est le Vainqueur")
else:
    print("\n\n",Player1.pseudo, "est le Vainqueur")

