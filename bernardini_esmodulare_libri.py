def inserisci_libro() -> dict:
    pass

def aggiungi_libro(lista: list, libro_aggiunto: dict) -> list:
    pass

def visualizza_libri(lista: list) -> None:
    pass

def rimuovi_libro(lista: list, libro_rimosso: dict) -> list:
    pass

def cerca_libro_autore(lista: list, autore: str) -> list[dict]|None:
    pass

def cerca_libro_titolo(lista: list, titolo: str) -> dict|None:
    pass

def main(lista: list):
    lista = []
    inserisci_libro()
    scelta = input("Scegli l'azione, 1 aggiungi, 2 rimuovi, 3 visualizza, 4 cerca per autore, 5 cerca per titolo: ")
    match scelta:
        case 1:
            aggiungi_libro()
        case 2:
            rimuovi_libro()
        case 3:
            visualizza_libri()
        case 4:
            cerca_libro_autore()
        case 5:
            cerca_libro_titolo()
            