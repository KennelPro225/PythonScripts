from os import chdir
from tkinter import*
from password_random import password
def reader():
    chdir("c:\password")
    with open("Password.txt","r+") as file:
        lec = file.readlines()
        a = len(lec)
        c = a - 1
        while c>0:
            b = lec[c]
            c -= 1
    
        return b

def generator():
    
    password()
    text = "votre mot de passe est: {}".format(password())
    texlabel = Label(root, text=text,bg="white",fg = "green").grid(row= 8,column=10)

root = Tk()
root.minsize(360,240)
root.maxsize(1080,360)
root.title('Générateur de Mot de Passe')

textbutton = "Générer un mot de passe"
bouton = Button(root,text= textbutton,bg= "black", fg= "white",command= generator)
bouton.grid(row=6,column=6)



mainloop()