be = 0
running = True
while running:
    print("Veuillez entrer un nombre")
    num = float(input())
    a = num
    if num == 0:
        break
    
    elif be < a:
        be = a
    elif be > a:
        a = be

be = int(be)
a = int(a)
if be > a:
    print('Le plus grand est:{}'.format(be))
else:
    print("Le plus grand est:{}".format(a))


