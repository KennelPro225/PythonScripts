
import tkinter as tk
from tkinter.ttk import Combobox
# from mysql.connector import
from datetime import date
from time import strftime

# the time
current_date = date.today()
current_time=strftime('%H:%M:%S')


# 
# class Registration(object):
#     "the object that's going to register the visitor"
#     def __init__(self,nom="None" ,prenom="None",mail="None@gmail.com",school="None",field="None",occupation="None",number=1234567890,purpose="None",gender="None",day=current_date,time=current_time):
#         self.nom = nom
#         self.prenom = prenom
#         self.mail = mail
#         self.school = school
#         self.field = field
#         self.occupation = occupation
#         self.number = number
#         self.purpose = purpose
#         self.gender = gender
#         self.day = day
#         self.time = time
        
#     def connexionfunc(self,nom="None" ,prenom="None",mail="None@gmail.com",school="None",field="None",occupation="None",number=1234567890,purpose="None",gender="None",day=current_date,time=current_time):
#         def detroy():
#             global family_name
#             global surname
#             global mail
#             global University
#             global Subject
#             global Purpose
#             global Phone_number

#             family_name.delete(0,tk.END)
#             surname.delete(0,tk.END)
#             mail.delete(0,tk.END)
#             University.delete(0,tk.END)
#             Subject.delete(0,tk.END)
#             Purpose.delete(0,tk.END)
#             Phone_number.delete(0,tk.END)
#         try:
#             con = connect(host='localhost',database='AMS', user='root', password='AKAKASSI')
#             cursor= con.cursor()
#             req = 'INSERT INTO visitors(id_visitor,visitor_lastname,visitor_firstname,visitor_gender,visitor_mail,visitor_phone,visitor_occupation,visitor_school,visitor_field,visitor_purpose,sdate,stime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#             infos = (cursor.lastrowid,nom,prenom,gender,mail,number,occupation,school,field,purpose,day,time)
#             view = cursor.execute(req,infos)
#             destroy()

#         except Error as err:
#             print(err)

#         finally:

#             if (con.is_connected()):
#                 cursor.close()
#                 con.close()
#             else:
#                 print("Base de donnée pas connectée")
#             return print("Bien Connecté")
        


root = tk.Tk()

# Background of the window
root.configure(background="#001225")

# The window's size regulation
root.minsize(1360,690)
root.maxsize(1360,695)

# The title of program
root.title("Registration's Page")

# The icon of the program
root.iconbitmap(("./icon.ico"))

# The frame that's going to contain the The Label and the Logo
frame = tk.Frame(root,bg="#001225",width=1200,height=180,bd=0)
# Frame.grid(row=0,column=2,pady=0)
frame.pack(side="top")

# Insert image
image= tk.PhotoImage(file="Logo1.png")
canvas= tk.Canvas(frame,bg="#706F6F",bd=0,width=1000,height=160,highlightthickness=0)
canvas.create_image(0,0,image=image,anchor="nw")
canvas.grid(row=0,column=1,padx=180)

# Frame 2 for the entries
frame1= tk.Frame(root,bg="#001225",width=1200,height=50)
# Frame1.grid(row=1,column=1,pady=150)
frame1.pack(pady=25)

# Entry Conception and label
First_name= tk.Label(frame1,text="First name",fg="#fff",bg="#001225")
First_name.grid(row=0,column=1,columnspan=3,padx=150)


Last_name= tk.Label(frame1,text="Last name",fg="#fff",bg="#001225")
Last_name.grid(row=0,column=2,padx=200)


Email= tk.Label(frame1,text="E-mail",fg="#fff",bg="#001225")
Email.grid(row=0,column=3,padx=200)


family_name = tk.Entry(frame1,width=35,borderwidth=3)
family_name.grid(row=2,column=1,columnspan=3,padx=150)


surname = tk.Entry(frame1,width=35,borderwidth=3)

surname.grid(row=2,column=2,padx=200)


mail = tk.Entry(frame1,width=35,borderwidth=3)
mail.grid(row=2,column=3,padx=200)


# Frame 3 for the entries
frame2= tk.Frame(root,bg="#001225",width=1200,height=50)
frame2.pack(pady=25)

# Entry Conception and label
School= tk.Label(frame2,text="School",fg="#fff",bg="#001225")
School.grid(row=0,column=2,padx=200)

Field = tk.Label(frame2,text="Field Of Study",fg="#fff",bg="#001225")
Field.grid(row=0,column=2,columnspan=3,padx=150)

Occupation = tk.Label(frame2,text="Occupation",fg="#fff",bg="#001225")
Occupation.grid(row=0,column=3,padx=200)

# Entries
option=[
    "Student",
    "Teacher",
    "Worker",
]
variable=tk.StringVar()

drop = Combobox(frame2,value=option,width=33,height=9)
drop.grid(row=2,column=3,padx=200)

drop.set("Student")


University = tk.Entry(frame2,width=35,borderwidth=3)
University.grid(row=2,column=2,padx=200)


Subject = tk.Entry(frame2,width=35,borderwidth=3)
Subject.grid(row=2,column=1,columnspan=3,padx=150)

# Frame 4  for Entries and labels and Radio_button
frame3 = tk.Frame(root,bg="#001225",width=1200,height=50)
frame3.pack(pady=25)

#Entries ,label and radio_button for the frame 4
Phone_number = tk.Entry(frame3,width=35,borderwidth=3)
Phone_number.grid(row=2,column=1,padx=150,columnspan=3,rowspan=2)

Purpose = tk.Entry(frame3,width=35,borderwidth=3)
Purpose.grid(row=2,column=2,padx=200)

phone= tk.Label(frame3,text="Phone Number",fg="#fff",bg="#001225")
phone.grid(row=0,column=2,padx=200)

purpose = tk.Label(frame3,text="Purpose",fg="#fff",bg="#001225")
purpose.grid(row=0,column=2,columnspan=3,padx=150)

gender = tk.Label(frame3,text="Gender",fg="#fff",bg="#001225")
gender.grid(row=0,column=3,padx=200)

#Menu for the gender
option1=[
    "Female",
    "Male",
]
variablesex=tk.StringVar()
sexe = Combobox(frame3,value=option1,width=33,)
sexe.grid(row=2,column=3,padx=200)

sexe.set("Female")


# Button's Frame4
frame4 = tk.Frame(root,bg="#001225",width=1200,height=50)
frame4.pack(pady=25)

# Button for validating
bouton= tk.Button(frame4,text="Validate",width=28,borderwidth=3,border=3,command=lambda:Registration.connexionfunc(self='',nom=family_name.get(),prenom=surname.get(),mail=mail.get(),school=University.get(),field=Subject.get(),occupation=drop.get(),number=Purpose.get(),purpose=Phone_number.get(),gender=sexe.get()))
bouton.grid(row=1,column=2,padx=500,pady=25)

root.mainloop()