from os import chdir

def gest_string(variable):
    try:
        variable =int(variable)
    except:
        pass
    else:
        a = print("Vous avez saisi un mauvais caractère: Utilisez des lettres")
        return a

def gest_integer(variable):
    try:
        test = variable + " "
    except:
        pass
    else:
        a = print("Vous avez entrée un mauvais caractère: Utilisez des entiers")
        return a


while True:
    nom = input("Veuillez entrez votre nom svp!!\t")
    c = gest_string(nom)
    if c == True:
        break


while True:
    prenom = input("Veuillez entrer votre Prénom svp!!")
    b = gest_string(prenom)
    if b == True:
        break

while True:
    age = int(input("Veuillez entrer votre âge svp!!"))
    a = gest_integer(age)
    if a == True:
        break


chdir("C:\Python")
base = str(nom)+" "+ str(prenom)+" "+ str(age)+";\n"
with open("enregistrement.txt","a+") as file:
    file.writelines(base)
    file.close()