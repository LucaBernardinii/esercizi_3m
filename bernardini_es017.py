#Scrivere un programma che passati in input n valori popoli una lista.
#In seguito chiede all'utente di inserire un valore in modo tale da verificare che esso sia presente nella lista. 
#Stampare a video ("Valore presente"/"Valore non presente").

lista_valori = []
nvalori = int(input("Inserisci il numero di valori: "))

for i in range(nvalori):
    valore = float(input("Inserisci un valore: "))
    lista_valori.append(valore)

verifica = float(input("Inserisci un valore per la verifica: "))

if verifica in lista_valori:
    print("Valore presente.")
else:
    print("Valore non presente.")
    