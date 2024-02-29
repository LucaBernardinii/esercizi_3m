#Gestione di una Azienda:
#Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:
#1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
#2. Stampa la lista di dipendenti.
#3. Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
#4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
#5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
#6. Stampa  le ore lavorate totali e il budget rimanente per ogni progetto.
#Questo esercizio richiede una gestione avanzata delle liste e dei dizionari, tenendo conto sia delle risorse umane che di quelle finanziarie. Buona gestione aziendale!

dipendenti = []
progetti = []
progetti_dipendenti = []

dipendente1 = {"nome": "Gigi", "ruolo": "stagista", "stipendio": 200, "ore": 5}
dipendente2 = {"nome": "Gino", "ruolo": "caporeparto", "stipendio": 2700, "ore": 10}
dipendente3 = {"nome": "Giorgio", "ruolo": "dipendente", "stipendio": 1400, "ore": 8}
dipendente4 = {"nome": "Giulia", "ruolo": "dipendente", "stipendio": 1200, "ore": 6}

dipendenti.append(dipendente1)
dipendenti.append(dipendente2)
dipendenti.append(dipendente3)
dipendenti.append(dipendente4)

print(dipendenti)

progetto = {"nome": "progetto_case", "Budget": 10000, "Costo orario": 300, "Durata": 480}

progetti.append(progetto)

associazione1 = {"nome_dipendente": "Gigi", "nome_progetto": "progetto_case", "ore_lavorate": 30}
associazione2 = {"nome_dipendente": "Giorgio", "nome_progetto": "progetto_case", "ore_lavorate": 40}
associazione3 = {"nome_dipendente": "Gino", "nome_progetto": "progetto_case", "ore_lavorate": 60}
associazione4 = {"nome_dipendente": "Giulia", "nome_progetto": "progetto_case", "ore_lavorate": 50}

progetti_dipendenti.append(associazione1)
progetti_dipendenti.append(associazione2)
progetti_dipendenti.append(associazione3)
progetti_dipendenti.append(associazione4)

for x in progetti_dipendenti:
    if x["nome_progetto"] == "progetto_case":
        print(x["nome_dipendente"], x["ore_lavorate"])

dipendente1["stipendio"] = (associazione1["ore_lavorate"] * progetto["Costo orario"]) + dipendente1["stipendio"]
dipendente2["stipendio"] = (associazione3["ore_lavorate"] * progetto["Costo orario"]) + dipendente2["stipendio"]
dipendente3["stipendio"] = (associazione2["ore_lavorate"] * progetto["Costo orario"]) + dipendente3["stipendio"]
dipendente4["stipendio"] = (associazione4["ore_lavorate"] * progetto["Costo orario"]) + dipendente4["stipendio"]

for x in dipendenti:
    print(x["nome"], x["stipendio"])

