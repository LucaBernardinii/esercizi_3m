#Progettare un applicativo che permetta di gestire il parco auto di una azienda di noleggio.
#Si consiglia di creare un dizionario al fine di modellare le caratteristiche/attributi di ogni singola auto(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero). Il parco auto sarà quindi memorizzato in una lista.
#L'applicativo dovrà permettere:
#1)aggiunta/rimozione di un veicolo
#2)Calcolo del bollo 
#3)Profitto del veicolo[giorno_affitto*(prezzo_giornaliero-IVA)- costo_gestione-bollo]
#4)Profitto (prima delle tasse) di tutto il parco auto
#
#Per il calcolo del bollo si consideri:
#2,58 euro a kW fino a 100kW
#3,87 euro per i kW eccedenti
#aggiungere 
#20 a kW oltre i 185kW

parco_auto = []

auto1 = {"marca": "Fiat",
         "modello": "500",
         "cilindrata": "500",
         "potenza_kw": "100",
         "anno_immatricolazione": "2007",
         "costo_gestione": "1500",
         "giorni_affitto": "10",
         "prezzo_giornaliero": "50"
         }

parco_auto.append(auto1)

scelta = input("Scegli un opzione: ")

match scelta:
    case 1:
        scelta2 = input("1 per aggiungere auto, 2 per rimuovere auto: ")
        match scelta2:
            case 1:
                auto2 = {"marca": input("Inserisci la marca: "),
                         "modello": input("Inserisci il modello: "),
                         "cilindrata": input("Inserisci la cilindrata: "),
                         "potenza_kw": input("Inserisci la potenza in kw: "),
                         "anno_immatricolazione": input("Inserisci l'anno d'immatricolazione: "),
                         "costo_gestione": input("Inserisci il costo di gestione: "),
                         "giorni_affitto": input("Inserisci i giorni di affito: "),
                         "prezzo_giornaliero": input("Inserisci il prezzo giornaliero: ")
                         }
            case 2:
                parco_auto.remove(input("Inserisci l'auto da rimuovere: "))
    case 2:
        bollo = (auto1["potenza_kw"] * 2,58)
        print(f"Il costo del bollo è {bollo}")
    case 3:
        bollo = (auto1["potenza_kw"] * 2,58)
        profitto_veicolo = ((auto1["giorni_affitto"]*auto1["prezzo_giornaliero"])-(auto1["costo_gestione"]-bollo))
        print(f"Il profitto del veicolo è {profitto_veicolo}")