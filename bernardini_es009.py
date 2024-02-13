#Dato in input il numero di secondi dire a quanti anni, mesi, giorni, ore, minuti e secondi corrispondono

secs = int(input("Insert seconds: "))

anno = secs // 31104000
restoanni = secs % 31104000
mese = restoanni // 2592000
restomesi = restoanni % 2592000
giorno = restomesi // 86400
restogiorni = restomesi % 86400
ora = restogiorni // 3600
restoore = restogiorni % 3600
minuto = restoore // 60
restominuti = restoore % 60
secondo = restominuti // 1

print(f"{secs} seconds are equal to {anno} years, {mese} months, {giorno} days, {ora} hours, {minuto} minutes and {secondo} seconds.")
