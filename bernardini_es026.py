#Equazione secondo grado

import math

def myinput():
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

    return a,b,c

def elaborazione(a,b,c):
    delta = b*b-4*a*c

    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print(x1,x2)
    elif delta == 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = x1
        print(x1,x2)
    else:
        print("Impossibile")

a,b,c = myinput()
print(a,b,c)