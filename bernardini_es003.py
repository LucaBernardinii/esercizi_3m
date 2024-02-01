raggio = input("Inserire il raggio del cerchio: ")

raggio = float(raggio)

import math 
x = math.pi 

circonferenza = (raggio * 2)*x
area = (raggio**2)*x

circonferenza = float(circonferenza)
area = float(area)

print(f"La circonferenza è {circonferenza}, l'area è {area}")