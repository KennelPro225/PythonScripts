from tkinter import*

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Calculateur de masse corporelle')
        self.geometry('800x400')
        self.config(background='Blue')
        self.resizable(False, False)

    def zone1(self):
        self.frame = Frame(self,width=800,height=200, bg="white")
        self.frame.pack()


