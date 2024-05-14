def inserisci_articolo() -> str:
    pass

def aggiungi_articolo(lista: list) -> str:
    pass

def visualizza_lista(lista: list) -> list:
    pass

def rimuovi_articolo(lista: list):
    pass

def main(lista: list):
    lista = []
    inserisci_articolo()
    scelta = input("Scegli l'azione, 1 aggiungi, 2 rimuovi, 3 visualizza: ")
    match scelta:
        case 1:
            aggiungi_articolo()
        case 2:
            rimuovi_articolo()
        case 3:
            visualizza_lista()
            