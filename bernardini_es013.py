#Scrivere 10 volte la parola "ciao"
#Sommare i numeri da 10 a 20 (compresi gli estremi)
#Sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10

for x in range(1,11):
    print("Ciao")

somma1 = 0
for x in range(10,21,1):
    somma2 = (somma1 + x)
    print(somma2)

for x in range(2,31,2):
    somma2 = (somma1 + x)
    print(somma2)

moltiplicazione1 = 1 
for x in range(1,30):
    moltiplicazione2 = (moltiplicazione1 * x)
    print(moltiplicazione2)
    