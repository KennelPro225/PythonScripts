from tkinter import*
from password_random import password

def mot_de_passe():
    text = "Votre mot de passe est:{}".format(password())
    texte = Label(root,text = text,bg="white",fg="blue").pack()
root =Tk()
root.title("Generateur de mot de passe")
bouton= Button(root,text="Générer Mot de Passe",bg="black",fg= "white",command=mot_de_passe).pack()
mainloop()