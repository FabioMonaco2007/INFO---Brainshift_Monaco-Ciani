def apply_answer(score: int, is_correct: bool) -> int:
    """Aggiorna il punteggio attuale in base alla correttezza della risposta.
    
    Parametri:
    -score: Il punteggio attuale (int).
    -is_correct: Booleano che indica se la risposta è corretta.
    
    Restituisce:
    -Il nuovo punteggio aggiornato."""
    if is_correct:
        return score + 10
    else:
        #Penalità in caso di risposta sbagliata
        return score - 5