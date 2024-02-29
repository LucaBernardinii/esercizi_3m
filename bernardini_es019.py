#Dato in input un numero scritto con sistema di numerazione decimale (intero), calcolare la sua conversione in binario.
#Dato che la stampa a video del numero deve avvenire in ordine inverso da quello del calcolo, usare una lista per stampare il valore corretto.

num = int(input("Inserisci un numero: "))

num_binario = []

risultato = num
while not(risultato == 0):
    resto = risultato % 2
    risultato = risultato // 2
    num_binario.append(resto)
    print(num_binario)
    
num_binario.reverse()

print(f'Il numero {num} in binario vale: {num_binario}')
