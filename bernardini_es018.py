#Scrivere un programma che passati in input n valori popoli una lista.
#In seguito scorre lista con un for e ne calcola il valore medio, il massimo e il minimo.

lista_valori = []
nvalori = int(input("Inserisci il numero di valori: "))

for i in range(nvalori):
    valore = float(input("Inserisci un valore: "))
    lista_valori.append(valore)

valore_massimo = max(lista_valori)
print(f"Il valore massimo è: {valore_massimo}")

valore_minimo = min(lista_valori)
print(f"Il valore minimo è: {valore_minimo}")

valore_medio = (sum(lista_valori)/len(lista_valori))
print(f"Il valore medio è: {valore_medio}")
