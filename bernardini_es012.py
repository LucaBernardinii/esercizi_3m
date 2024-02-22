#Dati in input n valori, calcolarne la somma.
#Suggerimenti....
#Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.

nvalori = int(input("Inserisci il numero di valori: "))
somma = 0

for x in range(nvalori):
    valore = float(input("Inserisci un valore: "))
    somma += valore
print(f"La somma è: {somma}")
