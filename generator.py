import random
from models import Trial
from rules import compute_expected_answer

def generate_trial(rng: random.Random) -> Trial:
    """Crea un nuovo trial (prova) scegliendo valori casuali in modo riproducibile."""
    
    #Definiamo la stringa contenente tutte le lettere dell'alfabeto maiuscole
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Selezioniamo la posizione: 'TOP' o 'BOTTOM'.
    #Usiamo rng.choice() invece di random.choice() per usare il seed di main.py
    position = rng.choice(['TOP', 'BOTTOM'])
    
    #Selezioniamo una lettera a caso dalla stringa definita sopra
    letter = rng.choice(letters)
    
    #Selezioniamo un numero intero compreso tra 1 e 9 (inclusi)
    number = rng.randint(1, 9)

    #Questa funzione riceve i tre parametri appena estratti
    expected_answer = compute_expected_answer(position, letter, number)

    #Creiamo e restituiamo l'oggetto Trial con tutti i dati generati.
    #Assicurati che l'ordine dei parametri corrisponda a quello in models.py
    return Trial(
        position = position,
        letter = letter,
        number = number,
        expected_answer = expected_answer
    )