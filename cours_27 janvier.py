from os import chdir
while True:
    try:
        nom = input("Veuillez entrez votre nom svp\t")
        nom = int(nom)
    except:
        break
    else:
        print("Vous avez saisi un mauvais caractère: Utilisez des lettres")

while True:
    try:
        prenom = input("Veuillez entrer votre prénom svp\t")
        prenom =int(prenom)
    except:
        break
    else:
        print("Vous avez saisi un mauvais caractère: Utilisez des lettres")

while True:
    try:
        age = int(input("Veuillez entrer votre âge\t"))
        test = age + " "
    except:
        break
    else:
        print("Vous avez entrée un mauvais caractère: Utilisez des entiers")

chdir("C:\Python")
base = str(nom)+" "+ str(prenom)+" "+ str(age)+";\n"
with open("enregistrement.txt","a+") as file:
    file.writelines(base)
    file.close()