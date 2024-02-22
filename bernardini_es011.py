nome = str(input("Inserisca il suo cognome: "))
nfotocopie = int(input("Inserire il numero di fotocopie desiderate: "))
rilegatura = str(input("Si desisera la rilegatura? (S/N): "))

if nfotocopie >= 1 and nfotocopie <= 19:
    costo_unit = 0.10
elif nfotocopie >= 20 and nfotocopie <= 100:
    costo_unit = 0.08
elif nfotocopie > 100:
    costo_unit = 0.05
else:
    print("Errore")

if rilegatura == "S":
    costo_rilegatura = 1.80
elif rilegatura == "N":
    costo_rilegatura = 0
else:
    print("Errore")

costo_unit = float(costo_unit)
costo_tot = float(costo_unit * nfotocopie)+costo_rilegatura
costo_rilegatura = float(costo_rilegatura)

if rilegatura == "S":
    print(f"Gentile Sig. {nome} il suo preventivo è di {costo_tot} euro compresa la rilegatura.")
elif rilegatura == "N":
    print(f"Gentile Sig. {nome} il suo preventivo è di {costo_tot} euro.")
else:
    print("Errore")
   