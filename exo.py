import tkinter as tk


class CompteBancaire(object):
    "Simulation d'un compte Compte Bancaire"
    def __init__(self,nom_client= "Dupont",solde=1000):
        self.nom_client=nom_client
        self.solde = solde

    def depot(self,depot):
        self.solde+=depot
        print("Vous avez réçu: {} Francs CFA sur votre Compte. Votre nouveau solde est de: {} Francs CFA".format(depot,self.solde))

    def retrait(self,retrait):
        self.solde-=retrait
        print("Vous avez rétiré: {} Francs CFA de votre compte. Votre nouveau solde est de: {} Francs CFA".format(retrait,self.solde))

    def affiche(self):
        print("Nom:",self.nom_client,"\nSolde:",self.solde,"Francs CFA sur votre compte")

# Instanciation d'un objet
compte1 = CompteBancaire("Koffi",solde=0)
compte2 = CompteBancaire("Yao",solde=5000)
compte3 = CompteBancaire("Séraphin",solde=2500)


compte1.depot(50000)
print("----------------------------------------------------------------------------")
compte1.affiche()
print("----------------------------------------------------------------------------")
compte1.retrait(10000)
print("----------------------------------------------------------------------------")
compte1.affiche()


app = tk.Tk()
# print(dir(tk.Tk))
app.title("Ma belle Interface")
app.geometry("300x400")
app.resizable(False,False)

app.mainloop()

