from tkinter.ttk import Combobox
from tkinter import*


class Applicattion(Tk):
    def __init__(self):
        Tk.__init__(self)
        # Configuration de la couleur
        self.config(background="#001225")
        self.geometry('1370x695')

        # eveneement de fullscreen
        self.bind('<Control-F>', self.fullscreen_func)

        # evenement de quit fullscreen
        self.bind('<Escape>', self.quitfullscreen_func)

        # evenement de validation
        self.bind('<Return>', self.validating)

    def validating(self, event):
        pass

    def quitfullscreen_func(self, event):
        self.attributes('-fullscreen', False)

    def fullscreen_func(self, event):
        self.attributes('-fullscreen', True)

    def zone1(self):
        self.frame = Frame(self, bg="#001225", width=1200, height=180, bd=0)
        self.frame.pack(pady=5, side='top')

        # insertion de l'image du haut qui presente le logo de l'american space
        self.picture = PhotoImage(file="Logo1.png")
        self.canvas = Canvas(self.frame, bg='white', bd=0,
                             width=1000, height=150, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.picture, anchor='nw')
        self.canvas.grid(padx=180)

    def zone2(self):
        self.frame1 = Frame(self, bg="#001225", width=1200, height=50)
        self.frame1.pack(pady=25)

        # création des labels pour les indications
        self.lastname_label = Label(
            self.frame1, text="Last name", fg='#fff', bg='#001225', font='Century')
        self.lastname_label.grid(row=0, column=1, columnspan=3, padx=150)

        self.name_label = Label(
            self.frame1, text='First Name', fg='#fff', bg='#001225', font='Century')
        self.name_label.grid(row=0, column=2, padx=200)

        self.mail_label = Label(self.frame1, text='Email',
                                fg='#fff', bg='#001225', font='Century')
        self.mail_label.grid(row=0, column=3, padx=200)

        # création des Entry pour la saisie des informations
        self.lastname_entry = Entry(self.frame1, width=35, borderwidth=3)
        # self.lastname_entry.insert(0,'Nom de famille')
        self.lastname_entry.grid(
            row=2, column=1, columnspan=3, padx=150, pady=8)

        self.name_entry = Entry(self.frame1, width=35, borderwidth=3)
        # self.name_entry.insert(0,"Prenoms")
        self.name_entry.grid(row=2, column=2, padx=200, pady=8)

        self.mail_entry = Entry(self.frame1, width=35, borderwidth=3)
        # self.mail_entry.insert(0,'Mail')
        self.mail_entry.grid(row=2, column=3, padx=200, pady=8)

    def zone3(self):
        self.frame2 = Frame(self, bg='#001225', width=1200, height=50)
        self.frame2.pack(pady=25)

        # création des labels pour les indications
        self.occupation_label = Label(
            self.frame2, text='Occupation', fg='#fff', bg="#001225", font='Century')
        self.occupation_label.grid(row=0, column=2, padx=250,)

        self.school_label = Label(
            self.frame2, text="School or Structure", fg="#fff", bg="#001225", font='Century')
        self.school_label.grid(row=0, column=1, columnspan=3, padx=200,)

        self.field_label = Label(
            self.frame2, text='Field Of Study', fg='#fff', bg='#001225', font='Century')
        self.field_label.grid(row=0, column=3, padx=250,)

        # Combobox pour les différentes ocuupation
        self.occupation_option = ["Student", "Teacher", "Worker", "Volunteer"]
        self.variable = StringVar()

        self.occupation_combobox = Combobox(
            self.frame2, value=self.occupation_option, width=33, height=9, textvariable=self.variable)
        self.occupation_combobox.grid(row=2, column=2, padx=200, pady=8)
        self.occupation_combobox.set(self.occupation_option[1])

        # création des entry pour la saisie des informations
        self.school_entry = Entry(self.frame2, width=35, borderwidth=3)
        # self.school_entry.insert(0,'Ecole ou strcuture')
        self.school_entry.grid(row=2, column=1, columnspan=3, padx=150, pady=8)

        self.field_entry = Entry(self.frame2, width=35, borderwidth=3)
        # self.field_entry.insert(0,'Filière')
        self.field_entry.grid(row=2, column=3, padx=200, pady=8)

    def zone4(self):
        self.frame3 = Frame(self, bg="#001225", width=1200, height=50)
        self.frame3.pack(pady=25)

        # creation des labels pour l'indication  des differents champs
        self.purpose_label = Label(
            self.frame3, text='Purpose', fg="#fff", bg="#001225", font='century')
        self.purpose_label.grid(row=0, column=2, padx=280,)

        self.phone_label = Label(
            self.frame3, text='Phone Number', fg="#fff", bg="#001225", font='century')
        self.phone_label.grid(row=0, column=1, columnspan=3, padx=200,)

        self.gender_label = Label(
            self.frame3, text='Gender', fg='#fff', bg='#001225', font='century')
        self.gender_label.grid(row=0, column=3, padx=280,)

        # creation des comboobox pour la selection des informations
        self.purpose_option = ['Reading Book',
                               'Class Attending', 'Computer Using', 'Formation']
        self.variable1 = StringVar()

        self.purpose_combobox = Combobox(
            self.frame3, values=self.purpose_option, width=33, height=9, textvariable=self.variable1,)
        self.purpose_combobox.grid(row=2, column=2, padx=200, pady=8)
        self.purpose_combobox.set(self.purpose_option[0])

        self.gender_option = ['Female', 'Male']
        self.variable2 = StringVar()
        self.gender_combobox = Combobox(
            self.frame3, values=self.gender_option, width=33, height=9, textvariable=self.variable2)
        self.gender_combobox.grid(row=2, column=3, padx=200, pady=8)
        self.gender_combobox.set(self.gender_option[0])

        # Entry pour la saisie d'information
        self.phone_entry = Entry(self.frame3, width=35, borderwidth=3)
        # self.phone_entry.insert(0,'Phone Number')
        self.phone_entry.grid(row=2, column=1, padx=150,
                              columnspan=3, rowspan=2, pady=8)

    def zone5(self):
        self.frame4 = Frame(root, bg="#001225", width=1200, height=50)
        self.frame4.pack(pady=25)

        # bouton de validation
        self.bouton = Button(self.frame4, text="Validate",
                             width=28, borderwidth=3, border=3, font='century')
        self.bouton.grid(row=1, column=2)


class Registrations():
    def __init__(self, lastname="None", firstname='None', mail='None@gmail.com', occupation='None', school='None', field='None', purpose='none', number=1234567890, gender='none'):
        self.lastname = lastname
        self.firstname = firstname
        self.mail = mail
        self.occupation = occupation
        self.school = school
        self.field = field
        self.purpose = purpose
        self.number = number
        self.gender = gender


root = Applicattion()

root.zone1()
root.zone2()
root.zone3()
root.zone4()
root.zone5()

root.mainloop()
