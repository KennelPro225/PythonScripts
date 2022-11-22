# from mysql.connector import

class Registration(object):
    "the object that's going to register the visitor"
    def __init__(self,nom="None" ,prenom="None",mail="None@gmail.com",school="None",field="None",occupation="None",number=1234567890,purpose="None",gender="None",day=current_date,time=current_time):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.school = school
        self.field = field
        self.occupation = occupation
        self.number = number
        self.purpose = purpose
        self.gender = gender
        self.day = day
        self.time = time
        
    def connexionfunc(self,nom="None" ,prenom="None",mail="None@gmail.com",school="None",field="None",occupation="None",number=1234567890,purpose="None",gender="None",day=current_date,time=current_time):
        def detroy():
            global family_name
            global surname
            global mail
            global University
            global Subject
            global Purpose
            global Phone_number

            family_name.delete(0,tk.END)
            surname.delete(0,tk.END)
            mail.delete(0,tk.END)
            University.delete(0,tk.ENDD)
            Subject.delete(0,tk.END)
            Purpose.delete(0,tk.END)
            Phone_number.delete(0,tk.END)
        try:
            con = connect(host='localhost',database='AMS', user='root', password='AKAKASSI')
            cursor= con.cursor()
            req = 'INSERT INTO visitors(id_visitor,visitor_lastname,visitor_firstname,visitor_gender,visitor_mail,visitor_phone,visitor_occupation,visitor_school,visitor_field,visitor_purpose,sdate,stime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            infos = (cursor.lastrowid,nom,prenom,gender,mail,number,occupation,school,field,purpose,day,time)
            view = cursor.execute(req,infos)
            detroy()

        except Error as err:
            print(err)

        finally:

            if (con.is_connected()):
                cursor.close()
                con.close()
            else:
                print("Base de donnée pas connectée")
            return print("Bien Connecté")