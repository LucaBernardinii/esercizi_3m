#Your task is to write a Python program that performs the following operations:
#Display the current inventory of products with their prices and quantities.
#Ask the user for a product, a price, and a quantity. Add the product, its price, and its quantity to the products, prices, and quantities lists respectively. If the product already exists in the products list, update its price and quantity in the prices and quantities lists respectively.
#Ask the user for a product to remove from the inventory. Remove the product, its price, and its quantity from the products, prices, and quantities lists respectively.
#Display the updated inventory of products with their prices and quantities.
#Calculate the total inventory by summing up the quantities of all products.
#Calculate the total value of the stocks by multiplying the price of each product by its quantity and summing up the results.

import os

inventario = {"prodotti": "laptop" "mouse" "keyboard",
             "prezzi": "1000" "70" "50",
             "quantità": "5" "10" "8"
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""
    Scegliere l'opzione desiderata:
    1) Visualizza inventario
    2) Aggiungi prodotto, prezzo e quantità.
    3) Rimuovi prodotto
    4) Totale inventario
    5) Valore totale inventario
    Scelta:""")

    scelta = input("Scegli l'opzione: ")

    match scelta: 
        case "1":
            for x in (inventario):
                print(inventario ["prodotti"])
                print(inventario ["prezzi"])
                print(inventario ["quantità"])
        case "2":
            prodotto = input("Inserisci un nuovo prodotto: ")
            prezzo = input("Inserisci un nuovo prezzo: ")
            quantità_2 = input("Inserisci una nuova quantità: ")
            
            inventario["prodotti"] = prodotto
            inventario["prezzo"] = prezzo
            inventario["quantità"] = quantità_2
        case "3":
            oggetto = input("Inserisci l'oggetto: ")
            if oggetto in inventario:
                inventario.pop(oggetto)
            else:
                print("Oggetto non trovato.")
        case "4":
            for x in (inventario):
                prodotto = inventario["prodotti"]
                quantità_2 = inventario["quantità"]
                
                totale = prodotto + quantità_2
                print(f"Il totale degli oggetti nell'inventario è: {totale}")
        case "5":
            for x in (inventario):
                prezzo = inventario["prezzi"]
                quantità_2 = inventario["quantità"]
                
                valore_totale = (prezzo * quantità_2) + (prezzo + quantità_2)
                print(f"Il valore totale degli oggetti nell'inventario è: {valore_totale}")
    input("Premi invio per continuare")
