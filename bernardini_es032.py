#lista1 = [45,75,25,68,98,12,21,84,54,62]
#lista2 = [42,78,23,74,95,16,27,88,51,66]
#lista3 = [
#    {"name":"Giovanni",
#     "surname":"Di Santo",
#     "age":42},
#     {"name":"Giuseppe",
#     "surname":"Mancini",
#     "age":75},
#     {"name":"Laura",
#     "surname":"Accardi",
#     "age":25},
#     {"name":"Lalla",
#     "surname":"Sallusti",
#     "age":68},
#     {"name":"Salvo",
#     "surname":"Olivieri",
#     "age":12},
#    ]
#
#
#Date le seguenti liste:
#1) ordinare la prima in ordine crescente
#2) ordinare la seconda in ordine decrescente
#3) ordinare la terza per età decrescente
#4) ordinare la terza in base alla lunghezza del cognome

lista1 = [45,75,25,68,98,12,21,84,54,62]
lista2 = [42,78,23,74,95,16,27,88,51,66]
lista3 = [
    {"name":"Giovanni",
     "surname":"Di Santo",
     "age":42},
     {"name":"Giuseppe",
     "surname":"Mancini",
     "age":75},
     {"name":"Laura",
     "surname":"Accardi",
     "age":25},
     {"name":"Lalla",
     "surname":"Sallusti",
     "age":68},
     {"name":"Salvo",
     "surname":"Olivieri",
     "age":12},
    ]


lista1.sort()
print(lista1)

lista2.sort(reverse=True)
print(lista2)

def età(e):
  return e["age"]

lista3.sort(key=età,reverse=True)
print(lista3)

def cognome(e):
  return e["surname"]

lista3.sort(len(key=cognome))
print(lista3)