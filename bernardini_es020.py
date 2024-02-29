#Scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un menu così formato:
#Scegliere l'opzione desiderata:
#1) Visualizza lista
#2) Aggiungi item e quantità
#3) Modifica quantità di un item
#4) Rimuovi item
#5) Esci
#Scelta:_

import os

lista_oggetti = []
lista_quantità = []


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
    Scegliere l'opzione desiderata:
    1) Visualizza lista
    2) Aggiungi item e quantità
    3) Modifica quantità di un item
    4) Rimuovi item
    5) Esci
    Scelta:""")
    
    scelta = input("Scelta:")
    match scelta:
        case '1':
            for oggetto, quantità in zip(lista_oggetti, lista_quantità):
                print(f"{oggetto}: {quantità}")
        case '2':
            oggetto = input("Inserisci l'oggetto: ")
            quantità = int(input("Inserisci la quantità: "))
            lista_oggetti.append(oggetto)
            lista_quantità.append(quantità)
        case '3':
            oggetto = input("Inserisci l'oggetto: ")
            if oggetto in lista_oggetti:
                quantità = int(input("Inserisci la nuova quantità: "))
                index = lista_oggetti.index(oggetto)
                lista_quantità[index] = quantità
            else:
                print("Oggetto non trovato.")
        case '4':
            oggetto = input("Inserisci l'oggetto: ")
            if oggetto in lista_oggetti:
                index = lista_oggetti.index(oggetto)
                lista_oggetti.pop(index)
                lista_quantità.pop(index)
            else:
                print("Oggetto non trovato.")
        case '5':
            break
        case _:
            print("Scelta non valida.")
    input("Premi invio per continuare.")