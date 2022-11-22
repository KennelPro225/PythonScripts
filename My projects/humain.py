from time import sleep
import turtle as t
running = True


lifetime = 3
sec = lifetime
"""
while running and sec >= 0:
    sleep(60)
    print("Il vous reste {} Minutes temps de vie".format(sec))

    
    sec -= 1
if sec == 0:
        print("Vous êtes mort. RIP")
"""

t.forward(12)
t.left(9)
t.color("red")
t.forward(8)
t.reset()
a = 0

while a <50:
    a = a +1
    t.forward(150)
    t.left(145)
