from flask import Flask, render_template
import json

def get_flashcard_by_id(id: int) -> None:
    with open("bernardini_es039_list.json", "r") as f:
        flashcards = json.load(f)
        for i in flashcards:
            if i["id"] == id:
                return i


def prompt_for_id() -> int:
    id = int(input("Inserisci un ID da 1 a 3: "))
    flashcard = get_flashcard_by_id(id)
    print(flashcard["question"])

def prompt_for_answer() -> str:
    risposta = str(input("Risposta: "))
    return risposta

def check_answer(risposta: str, risposta_corretta: str) -> bool:
    return risposta.lower == risposta_corretta.lower()

prompt_for_id()
risposta = prompt_for_answer()