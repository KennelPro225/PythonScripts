class Tasse(object):
    "Ma petite Tasse"
    pass

class Etudiant(object):
    "Classe definissant l'objet Etudiant"
    def __init__(self,nom = "Julian",prenom = "KING",yy=2000):
        self.datenaissance=yy
        self.nom = nom
        self.prenom = prenom

    def afficher_datenaissance(self):
        print(self.datenaissance)
    
    def calculer_age(self):
        age = 2022 - self.datenaissance
        print("Votre nom est:",self.nom,"\nvotre âge est:",age,"ans")

    def immatriculation(self):
        matricule = self.nom+self.prenom+str(self.datenaissance)
        print(matricule)




a = Etudiant(nom="Koffi",prenom="Yao",yy=2002)
b = Etudiant(nom="Yao",prenom="Celestin",yy=1994)
c = Etudiant(nom="Yeo",prenom="Adama",yy=1964)

c.nom="Blé"
c.datenaissance = 2000
b.afficher_datenaissance()
print("----------------------------------------------------------------------------")
c.calculer_age()
print("----------------------------------------------------------------------------")
c.immatriculation()
