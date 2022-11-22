from random import choice, random
import os
from app import checker

os.chdir("c:\\")
if not os.path.exists("Password"):
    os.mkdir("Password")

else:
    pass

lettercap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

lettersma = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

num = [1,2,3,4,5,6,7,8,9]

running  =  True
comp = 1
def password():
    while running and comp > 0:
        os.chdir("c:\password")
        a = choice(lettercap)
        b = choice(lettersma)
        c = choice(num)
        c = str(c)
        d = choice(num)
        d = str(d)
        e = choice(num)
        e = str(e)
        f = choice(num)
        f = str(f)
        g = choice(num)
        g = str(g)
        h = choice(lettercap)
        i = choice(lettercap)
        j = choice(num)
        j = str(j)
        k = choice(lettersma)
        l = choice(lettersma)
        mot_de_passe = a+ b + c + d + e + f + g + h + i + j + k + l + "\n"
        return mot_de_passe
    
        file = open("Password.txt","a")
        file.writelines(mot_de_passe)
        file.close()

        comp -=1

checker()