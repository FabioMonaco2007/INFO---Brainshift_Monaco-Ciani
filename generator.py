import random
from models import Trial
from rules import compute_expected_answer

def generate_trial(rng: random.Random) -> Trial:
    """Crea un nuovo trial (prova) scegliendo valori casuali in modo riproducibile."""
    
    #Definiamo la stringa contenente tutte le lettere dell'alfabeto maiuscole
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Selezioniamo la posizione: 'TOP' o 'BOTTOM'
    position = rng.choice(['TOP', 'BOTTOM'])
    
    #Selezioniamo una lettera a caso dalla stringa
    letter = rng.choice(letters)
    
    #Selezioniamo un numero intero compreso tra 1 e 9 (inclusi)
    number = rng.randint(1, 9)

    #Calcoliamo la risposta attesa usando la funzione corretta da rules.py
    expected_answer = compute_expected_answer(position, letter, number)

    #Creiamo e restituiamo l'oggetto Trial con tutti i dati generati
    return Trial(
        position = position,
        letter = letter,
        number = number,
        expected_answer = expected_answer
    )