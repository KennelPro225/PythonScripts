from tkinter import*
from webbrowser import open


# defintion de la commande
def calcul(poids,taille,year,sexe):
    global background
    # declaration des differentes variables Entry et Radiobutton
    poids= int(weight.get())
    taille = int(size.get())/10
    year = int(age.get())
    sexe= int(v.get())
    # calcul de l'IMC et l'IMG formule
    IMC = round(((poids/taille)**2),2)
    A = 1.2 * IMC
    B = 0.23 * year
    C = 10.8 * sexe
    IMG = round((A + B - C - 5.4),2)
    
    # CONDITIONS POUR STATUER LE POIDS DE L'USER
    if IMC <= 16.5:
        text = "Vous êtes en Dénutrition"
    if 16.5< IMC <=18.5:
        text = "Vous êtes Maigre"
    if 18.5< IMC <=24.9:
        text = "vous avez un poids normal"
    if 25< IMC <= 29.9:
        text ="Vous êtes en surpoids"
    if 30< IMC <= 34:
        text = "Vous êtes en obesité modérée"
    if 35< IMC <=39.9:
        text = "Vous êtes en obésité sévère"
    if IMC>40:
        text = "Vous êtes en obésité massive"
    
    # resulat des  calculs et le bilan
    label = Label(root,text="Votre IMG est de{}%\nVotre IMC est de:{}Kg/m-²".format(IMG,IMC),bg="#A2B791",fg="white").pack(pady=0,side=TOP)#.grid(row=0,column=1)

    # bouton qui redirige vers une page web et un label qui presente le statut
    label1 = Label(root,text=text,bg="#A2B791",fg="white").pack(side=TOP,pady=15)
    bouton = Button(root,text="Plus d'info",width=10,command=info).pack(side=TOP,pady=25)
    
    boutonB = Button(root,text="Calculer encore",width=13, command=recurs).pack(side=TOP,pady=15)

    # suppression des items
    weight.destroy()
    size.destroy()
    age.destroy()
    sex1.destroy()
    sex2.destroy()
    boutonA.destroy()

def recurs():
    label1.destroy()
    label.destroy()
    bouton.destroy()
    boutonB.destroy()
    # commande des genres
    def femme(num):
        num= v.get()
        return num

    def homme(num):
        num= v.get()
        return num     
    # Des entry pour pouvoir récuperer les données saisies par l'utilisateur
        
    weight = Entry(root,width=23,borderwidth=2)
    weight.pack(pady=10,side=TOP)#grid(row=1,column=0,padx=5,pady=5)
    weight.insert(0,"Poids en Kg")
    size = Entry(root,width=23,borderwidth=2)
    size.insert(0,"Taille en Cm")
    size.pack(pady=10,side=TOP)#grid(row=2,column=0,padx=10,pady=10) 
    age = Entry(root,width=23,borderwidth=2)
    age.insert(0,"Age")
    age.pack(pady=10,side=TOP)#grid(row=3,column=0,padx=10,pady=10)

        # Bouton radio
    v = IntVar()
    sex1 = Radiobutton(root,width=23,text="Femme",variable=v,value=0,command=lambda:femme(v.get()))
    sex1.pack(pady=10,)#grid(row=4,column=0)
    sex2 =Radiobutton(root,width=23,text="Homme",variable=v,value=1,command=lambda:homme(v.get()))
    sex2.pack(pady=10,)#grid(row=5,column=0)

        # bouton pour afficher le resulat
    boutonA = Button(root, text="Voir résultat",width=10,command=lambda:calcul(weight.get(),size.get(),age.get(),v.get()))
    bouton.pack(pady=45,)#grid(row=3,column=2)



def info():
    open("https://www.e-sante.fr/minceur-3-conseils-pour-atteindre-un-imc-normal/actualite/615551")

# commande des genres
def femme(num):
    num = v.get()
    return num

def homme(num):
    num = v.get()
    return num

root= Tk()
root.title("BMI Calculator")#Le titre de la fenêtre
root.maxsize(720 ,600)#la taille maximale de la fenêtre 
root.minsize(720 ,600)#la taille minimale de la fenêtre
# couleur de fond
root.config(background="#A2B791") 

# text label de presentation
text = "Calculateur de Masse corporelle"
my_label= Label(root,text=text,bg="red",fg="white")
my_label.pack(side =TOP)#grid(row=0,column=0)
 
# insertion de l'image en fond
background = PhotoImage(file = "background.png") 
canvas1 = Canvas( root, width = 500, height = 500,bg="#A2B791") 
canvas1.pack(side=RIGHT) 
canvas1.create_image(0,0,image = background,anchor = "nw")

# Des entry pour pouvoir récuperer les données saisies par l'utilisateur
weight = Entry(root,width=23,borderwidth=2)
weight.pack(pady=10,side=TOP)#grid(row=1,column=0,padx=5,pady=5)
weight.insert(0,"Poids en Kg")
size = Entry(root,width=23,borderwidth=2)
size.insert(0,"Taille en Cm")
size.pack(pady=10,side=TOP)#grid(row=2,column=0,padx=10,pady=10) 
age = Entry(root,width=23,borderwidth=2)
age.insert(0,"Age")
age.pack(pady=10,side=TOP)#grid(row=3,column=0,padx=10,pady=10)

# Bouton radio
v = IntVar()
sex1 = Radiobutton(root,width=23,text="Femme",variable=v,value=0,command=lambda:femme(v.get()))
sex1.pack(pady=10,)#grid(row=4,column=0)
sex2 =Radiobutton(root,width=23,text="Homme",variable=v,value=1,command=lambda:homme(v.get()))
sex2.pack(pady=10,)#grid(row=5,column=0)

# bouton pour afficher le resulat
boutonA = Button(root, text="Voir résultat",width=10,command=lambda:calcul(weight.get(),size.get(),age.get(),v.get()))
boutonA.pack(pady=45,)#grid(row=3,column=2)


mainloop()