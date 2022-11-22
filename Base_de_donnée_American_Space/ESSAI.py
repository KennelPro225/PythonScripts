import tkinter as tk 
from tkinter import mainloop, ttk
def work():
    app = tk.Tk()

    app.geometry("200x200")

    labelTop= tk.Label(app,text="Are you a girl ou a boy?")
    labelTop.grid(column=0, row= 0)

    comboExample= ttk.Combobox(app,
                                value=[
                                    "Boy",
                                    "Girl"])

    # print(dict(comboExample))
    comboExample.grid(column=0,row=1)
    comboExample.current()
    print(comboExample.current(), comboExample.get())
    app;mainloop()