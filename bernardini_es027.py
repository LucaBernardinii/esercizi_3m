#Funzione 1:
#
#Scrivere una funzione che gestisca l'input di n valori (con n scelto dall'utente) e li restituisca in una lista.
#def input_n () -> list[int]:
#
#Funzione 2:
#Scrivere una funzione alla quale passato un numero intero restituisca True se esso è pari e False in caso contrario.
#def is_pari(num: int) ->bool:
#
#Funzione 3:
#Scrivere una funzione che data in input una lista. Calcoli la somma dei quadrati dei numeri pari presenti nella lista e restituisca tale valore.
#def somma_quadrati (lista_valori: list[int]) -> int:

def input_n () -> list[int]:
    n_valori = int(input("Inserisci il numero di valori da inserire: "))
    lista_valori = []
    for i in range(n_valori):
        num = input(f"Inserisci il numero {i+1}: ")
        lista_valori.append(num)
    return lista_valori
valori = input_n()
print(valori)

print("---------------------")

num = int(input("Inserisci un numero: "))

def pari (num: int) -> bool:
    num = num%2

    if num==0:
        return True
    else:
        return False
ris = pari(num)
print(ris)

print("---------------------")

