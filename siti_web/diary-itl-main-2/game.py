from Speech import speech
from random import randint, choice
from time import sleep

livelli = {
    "facile" : ["agenda", "ami", "souris"],
    "medio" : ["ordinateur", "algorithme", "développeur"],
    "difficile" : ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    words = livelli.get(level, [])
    if not words:
        print("Hai selezionato un livello errato")
        return
    score = 0
    num_attempts = 3  # Il numero di tentativi per parola

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Si prega di pronunciare la parola {random_word}")
        recog_word = speech()
        print("Hai pronunciato: "+recog_word)
        if random_word == recog_word:
            print("Hai indovinato")
            score += 1
        else:
            print("C'è qualcosa di sbagliato")
        
        sleep(2)
    
    print(f"Il gioco è finito! Il tuo punteggio è {score}/{len(words)}")

selected_level = input("Selezionare il livello di difficoltà (facile/medio/difficile):").lower()
play_game(selected_level)