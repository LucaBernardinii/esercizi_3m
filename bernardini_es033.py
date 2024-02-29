#Scrivere una programma che letto da file JSON una lista di dizionari contenenti le fatture di n utenti così formate:
#{"id":"id_utente",
#"importo":128.54,
#"sconto_fattura":15}
#svolga le seguenti funzioni:
#1) Mostri tutte le fatture 
#2) Permetta di aggiungere ad una fattura selezionata una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
#3)Permetta di aggiungere una fattura alla lista (aggiornando il file JSON)
#
#- Definire apposite funzioni di lettura e scrittura da/sul file JSON.
#- Definire eventuali altre funzioni utili ai fini dell'esercizio.

import json

with open("bernardini_es033.json", "r") as file_json:
    try:
        mylist = json.load(file_json)
    except:
        mylist = []

print(type(mylist))
print(mylist)

def aggiunta_importo_scontato(fatture: list, idx: int) -> list:
    fatture[idx]["importo_scontato"] = fatture[idx]["importo"] - (
        fatture[idx]["importo"] * fatture[idx]["sconto_fattura"] / 100
    )
    return fatture

aggiunta_importo_scontato(fatture,3)

mylist.append({"name":"Loredana",
               "surname":"Borselli",
               "age":45,
               "hobbies":["cars","music","computers"]})

with open("bernardini_es033.json","w") as file_json:
    json.dump(mylist,file_json,indent = 4)
