from tkinter import*
root = Tk()
textLabel = "BONJOUR JE SUIS KENNEL"
etiquette = Label(root, text = textLabel, fg = "green")
etiquette.pack(padx = 30, pady =20)
commandBouton = root.quit
bouton = Button(root, text="EXIT", command = commandBouton)

bouton.pack(pady=5)
