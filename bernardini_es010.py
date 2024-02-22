#Dati in input il voto in trentesimi e il numero di crediti di tre esami, calcolare la media ponderata

voto1 = float(input("Inserisci il primo voto: "))
credito1 = float(input("Inserisci il primo credito: "))
voto2 = float(input("Inserisci il secondo voto: "))
credito2 = float(input("Inserisci il secondo credito: "))
voto3 = float(input("Inserisci il terzo voto: "))
credito3 = float(input("Inserisci il terzo credito: "))

if 0 < voto1 <= 30 and 0 < voto2 <= 30 and 0 < voto3 <= 30:
    media = ((voto1 * credito1) + (voto2 * credito2) + (voto3 * credito3))/(credito1 + credito2 + credito3)
    print(f"La media è: {media}")
else:
     print("Errore")
     