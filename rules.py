def è_pari(numero: int) -> bool:
    """Verifica se un numero è pari, controllando prima se è un intero."""
    if isinstance(numero, int):
        return numero % 2 == 0
    raise ValueError("Il valore fornito non è un numero valido.")

def è_vocale(lettera: str) -> bool:
    """Verifica se è una vocale, controllando prima se è una stringa."""
    if isinstance(lettera, str):
        return lettera.lower() in ["a", "e", "i", "o", "u"]
    raise ValueError("Il valore fornito non è una lettera valida.")

def calcola_risposta_attesa(posizione: str, lettera: str, numero: int) -> bool:
    """Decide il controllo usando solo strutture condizionali if/else."""

    if not isinstance(posizione, str):
        raise ValueError("La posizione deve essere una parola (stringa).")

    pos = posizione.lower()
    
    if pos == "alto":
        return è_pari(numero)
    elif pos == "basso":
        return è_vocale(lettera)
    else:
        raise ValueError(f"Posizione non valida: {posizione}")
