import os
def checker():
    
    os.chdir("c:\password")
    with open("Password.txt","r+") as file:
        list = file.readlines()
        length = len(list)
        file.close()

    print(length)
    comp = 0
    b = ""
    running  = True
    while comp < length:
        os.chdir("c:\password")
    
        if list[comp] != b:
            b = list[comp]
        
        else:
            with open("Meme.txt","a") as file1:
                file1.writelines(b)
                file1.close()
        comp +=1
    