from tkinter import*

def number(num):
    a = str(num)
    return e.get(a)

root = Tk()
root.title("Calculatrice")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

bouton_1 = Button(root,text="1",bg="black",fg="white",width=10,height=4,command=lambda:number(1),relief= GROOVE)
bouton_2 = Button(root,text="2",bg="black",fg="white",width=10,height=4,command=lambda:number(2),relief= GROOVE)
bouton_3 = Button(root,text="3",bg="black",fg="white",width=10,height=4,command=lambda:number(3),relief= GROOVE)
bouton_4 = Button(root,text="4",bg="black",fg="white",width=10,height=4,command=lambda:number(4),relief= GROOVE)
bouton_5 = Button(root,text="5",bg="black",fg="white",width=10,height=4,command=lambda:number(5),relief= GROOVE)
bouton_6 = Button(root,text="6",bg="black",fg="white",width=10,height=4,command=lambda:number(6),relief= GROOVE)
bouton_7 = Button(root,text="7",bg="black",fg="white",width=10,height=4,command=lambda:number(7),relief= GROOVE)
bouton_8 = Button(root,text="8",bg="black",fg="white",width=10,height=4,command=lambda:number(8),relief= GROOVE)
bouton_9 = Button(root,text="9",bg="black",fg="white",width=10,height=4,command=lambda:number(9),relief= GROOVE)
bouton_0 = Button(root,text="0",bg="black",fg="white",width=10,height=4,command=lambda:number(9),relief= GROOVE)


bouton_add = Button(root,text="+",bg="white",fg="black",width=10,height=8,command=lambda:number(0),relief= GROOVE)
bouton_sub = Button(root,text="-",bg="white",fg="black",width=10,height=8,command=lambda:number(0),relief= GROOVE)
bouton_equal = Button(root,text="=",bg="black",fg="white",width=4,height=8,command=lambda:number(0),relief= GROOVE)

bouton_1.grid(row=3,column=0)
bouton_2.grid(row=3,column=1)
bouton_3.grid(row=3,column=2)
bouton_4.grid(row=2,column=0)
bouton_5.grid(row=2,column=1)
bouton_6.grid(row=2,column=2)
bouton_7.grid(row=1,column=0)
bouton_8.grid(row=1,column=1)
bouton_9.grid(row=1,column=2)
bouton_0.grid(row=4,column=0,rowspan=1)


#bouton_add.grid(row=,column=)
#bouton_sub.grid(row=,column=)
bouton_equal.grid(row=4,column=1)
mainloop()