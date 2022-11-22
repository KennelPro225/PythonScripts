import os

chemin = os.chdir("c:\\")

if not os.path.exists("Python"):
    os.mkdir("Python")

else:
    pass

def saisir(Nom_Prenom,Cin,Groupe,Age,Decision):
    global chemin
    os.chdir("c:\python")
    nom = Nom_Prenom
    num = Cin
    num =str(num)
    group = Groupe
    age = Age
    age = str(age)
    choix = Decision
    donnee = nom + " " + num + " " + group + " " + age + " " + choix + ";" + "\n"
    with open("Concours.txt","a+") as file:
        file.writelines(donnee)
        file.close()
    b = file
    return b

def admis(Nom_Prenom,Cin,Groupe,Age,Decision):
    global chemin
    os.chdir("c:\python")
    nom = Nom_Prenom
    num = Cin
    num =str(num)
    group = Groupe
    age = Age
    age = str(age)
    choix = Decision
    donnee = nom + " " + num + " " + group + " " + age + " " + choix + ";" + "\n"
    with open("Admis.txt","a+") as file:
        file.writelines(donnee)
        file.close()
    b = file
    return b

def attente(Nom_Prenom,Cin,Groupe,Age,Decision):
    global chemin
    os.chdir("c:\python")
    nom = Nom_Prenom
    num = Cin
    num =str(num)
    group = Groupe
    age = Age
    age = str(age)
    choix = Decision
    donnee = nom + " " + num + " " + group + " " + age + " " + choix + ";" + "\n"
    with open("Attente.txt","a+") as file:
        file.writelines(donnee)
        file.close()
    b = file
    return b

def refuse(Nom_Prenom,Cin,Groupe,Age,Decision):
    global chemin
    os.chdir("c:\python")
    nom = Nom_Prenom
    num = Cin
    num =str(num)
    group = Groupe
    age = Age
    age = str(age)
    choix = Decision
    donnee = nom + " " + num + " " + group + " " + age + " " + choix + ";" + "\n"
    with open("Refusé.txt","a+") as file:
        file.writelines(donnee)
        file.close()
    b = file
    return b

def statistiques(dec):
    
    os.chdir("c:\python")
    
    with open("Concours.txt","r+") as file3:
        list_file3 = file3.readlines()
        file3.close()
        length3 = len(list_file3)
    if dec == "Admis" or "admis":
        with open("Admis.txt","r+") as file1:
            
            list_admis = file1.readlines()
            length1 = len(list_admis)
            calcul1 = (length1/length3)*100
            file1.close()
            print(calcul1)
    
    elif dec == "Attente" or"attente":
        with open("Attente.txt","r+") as file2:
            
            list_file2 = file2.readlines()
            length2 = len(list_file2)
            calcul2 = (length2/length3)*100
            file2.close()
            print(calcul2)
    
    
    else:
        if dec == "refusé" or "Refusé":
            with open("Refusé.txt","r+") as file4:
                file4.readline()
                list_file4 = file4.readline()
                length4 = len(list_file4)
                calcul3 = (length4/length3)*100
                print(calcul3)

def supprime():
    pass#je ne sais pas comment m'arranger ow je n'ai pas pu faire cette fonction


running = True
fin = 10



while running and fin > 0:
    print("Veuillez Saisir Votre Nom et Prenom(s)")
    Nom_prenom = input()

    print("Numéro de CNI")
    Cin = (input())

    print("Votre Groupe svp?")
    Groupe = input()

    print("Veuillez Saisir Votre âge")
    Age = int(input())

    Decision_liste = ["Admis","Attente","Refusé"]

    if Age < 30:
        Decision = Decision_liste[0]
        b = admis(Nom_prenom,Cin,Groupe,Age,Decision)

    elif Age >= 30:
        Decision = Decision_liste[1]
        c = attente(Nom_prenom,Cin,Groupe,Age,Decision)
    else:
        d = refuse(Nom_prenom,Cin,Groupe,Age,Decision)

    a = saisir(Nom_prenom,Cin,Groupe,Age,Decision)
    
    fin -= 1

dec = input("Vous voulez voir le pourcentages de quelle décision? Admis-Refusé-Attente\t")

statistiques(dec)
