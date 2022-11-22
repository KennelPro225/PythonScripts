import tkinter


win = Tk()

v = StringVar()
def setText(Word):
    v.set(Word)

a = Button(win, text="plant", command=setText("plant")
a.pack()
b = Button(win, text="animal", command=setText("animal"))
b.pack()
c = Entry(win, textvariable=v)
c.pack()
win.mainloop()