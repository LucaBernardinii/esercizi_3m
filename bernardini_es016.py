#Scrivere un programma che passati in input n valori popoli una lista e la ristampi a video scorrendola con un for.

lista_valori = []
nvalori = int(input("Inserisci il numero di valori: "))

for i in range(nvalori):
    valore = float(input("Inserisci un valore: "))
    lista_valori.append(valore)

print(lista_valori)
