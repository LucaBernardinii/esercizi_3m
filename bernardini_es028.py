#Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), i kW e gli anni passati dall'immatricolazione di un autoveicolo, calcoli il bollo auto e l'eventuale superbollo.
#Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.
#
#N.B.
#Creare una funzione specifica per il superbollo da usare nella funzione principale.
#es.
#def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....
#
#Signature metodo principale:
#def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
#N.B.
#La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None
#
#
#utilizzo:
#bollo, superbollo = calcola_bollo (.......................................
#
#Calcolo bollo:
#Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
#Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
#Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
#Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
#Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Calcolo superbollo:
#Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
#Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
#Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
#Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
#Dopo i 20 anni non pagano il superbollo

def calcola_superbollo (kW:int, immatricolazione: int) ->float:   
        if kW > 185:
            if immatricolazione > 20:
                super_bollo = 0
            elif immatricolazione > 15 and immatricolazione <= 20:
                kW = kW - 185
                super_bollo = 3 * kW
            elif immatricolazione > 10 and immatricolazione <= 15:
                kW = kW - 185
                super_bollo = 6 * kW
            elif immatricolazione > 5 and immatricolazione <= 10:
                kW = kW - 185
                super_bollo = 12 * kW
            else:
                kW = kW - 185
                super_bollo = 20 * kW
        return super_bollo


def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None:    
    match classe_ambientale:
        case 0:
            if kW <= 100:
                bollo = 3 * kW
            else:
                bollo = 300 + (4.50*(kW-100))
        case 1:
            if kW <= 100:
                bollo = 2.9 * kW
            else:
                bollo = 300 + (4.35*(kW-100))
        case 2:
            if kW <= 100:
                bollo = 2.8 * kW
            else:
                bollo = 300 + (4.20*(kW-100))
        case 3:
            if kW <= 100:
                bollo = 2.7 * kW
            else:
                bollo = 300 + (4.05*(kW-100))
        case 4:
            if kW <= 100:
                bollo = 2.58 * kW
            else:
                bollo = 300 + (3.87*(kW-100))
        case 5:
            if kW <= 100:
                bollo = 2.58 * kW
            else:
                bollo = 300 + (3.87*(kW-100))
        case 6:
            if kW <= 100:
                bollo = 2.58 * kW
            else:
                bollo = 300 + (3.87*(kW-100))
    return bollo

classe_ambientale = int(input("Classe ambientale del veicolo, Euro: "))
kW = int(input("Inserisci la potenza in kW del veicolo: "))
immatricolazione = int(input("Inserisci gli anni passati dalla data di immatricolazione: ")) 
totale_bollo = calcola_bollo(classe_ambientale,kW,immatricolazione) + calcola_superbollo(kW,immatricolazione)

print(totale_bollo)