print("Quel âge avez-vous?")

age  = int(input())

if 6<=age<=9:
    print("Poussin")
elif 10<=age<=13:
    print("Pupille")
elif 14<=age<=16:
    print('Minime')
else:
    if age >= 17:
        print("Cadet")