#Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo.
#In particolare, l'applicativo dovrà permettere di:
#1) Creare una nuova stanza (id, denominazione, metratura) 
#2) Aggiungere un opera ad una stanza(titolo, artista, anno)
#3) Consultare le opere presenti in una stanza
#4) Consultare le stanze presenti
#5) Cercare le informazioni su un opera
#6) Cancellare un opera
#7) Cancellare una stanza solo se vuota

import os

museo = []
stanza = {}
opere = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("1 per creare una stanza,\n2 per aggiungere un'opera ad una stanza,\n3 per consultare le opere di una stanza,\n4 per consultare le stanze presenti,\n5 per consultare le informaxzioni di un'opera,\n6 per rimuovere un'opera,\n7 per cancellare una stanza se vuota.")

    scelta = input("Scegli l'azione da fare: ")

    match scelta:
        case "1":
            id = input("Inserisci id stanza: ")
            denominazione = input("Inserisci una denominazione: ")
            metratura = input("Inserisci la metratura: ")
            
            stanza = {"id": id,
                      "denominazione": denominazione,
                      "metratura": metratura,
                      "opere": []
                      }
            museo.append(stanza)            
        case "2":
            titolo = input("Inserisci titolo opera: ")
            artista = input("Inserisci l'artista: ")
            anno = input("Inserisci l'anno dell'opera: ")
            
            opera = {"titolo": titolo,
                     "artista": artista,
                     "anno": anno
                     }
            opere.append(opera)
            scelta_stanza = input("Scegli la stanza in cui assegnare l'opera: ")
            scelta_stanza.append(opera)
        case "3":
            print(opere)
        case "4":
            print(museo)
        case "5":
            print(opera)
        case "6":
            scelta_opera = input("Scegli l'opera da cancellare: ")
            opere.remove(scelta_opera)
        case "7":
            scelta_stanza2 = input("Scegli la stanza da cancellare: ")
            museo.remove(scelta_stanza2)
            