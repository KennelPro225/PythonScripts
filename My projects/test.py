print("Veuillez saisir Nom et Prenoms SVP!") 
nom_et_prenoms= input()
print("Bonjour", nom_et_prenoms, "Bienvenue à notre programme!")
print("Veuillez entrez votre poids en Kg SVP!")
poids = float(input())
poids = int(poids)
print("Veuillez entrez votre taille en m SVP! ")
taille = float(input())
print("Quel est votre âge?")
age = input()
age = int(age)
F = 0
M = 1
sexe = [F,M]

print("Quel est votre genre F ou M:", sexe)
sexe = input()
sexe = int(sexe)


"""
L' IMC est l'Indice de Masse Corporelle
IMC = poids/taille²
"""
IMC = poids / taille**2

print("Votre IMC est:", IMC, "Kg/m-²")
A = 1.2 * IMC
B = 0.23 * age
C = 10.8 * sexe

IMG = A + B - C - 5.4

print("Votre IMG est :", IMG, "%")
if IMC <= 16.5:
    print("Vous êtes en Dénutrition")
if 16.5< IMC <=18.5:
    print("Vous êtes Maigre")
if 18.5< IMC <=24.9:
    print("vous avez un poids normal")
if 25< IMC <= 29.9:
    print("Vous êtes en surpoids")
if 30< IMC <= 34:
    print("Vous êtes en obesité modérée")
if 35< IMC <=39.9:
    print("Vous êtes en obésité sévère")
if IMC>40:
    print("Vous êtes en obésité massive")    





    
