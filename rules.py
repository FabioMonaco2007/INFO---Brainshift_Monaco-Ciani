def is_even(number: int) -> bool:
    """Verifica se un numero è pari, controllando prima se è un intero."""
    if isinstance(number, int):
        return number % 2 == 0
    raise ValueError("Il valore fornito non è un numero valido.")

def is_vowel(char: str) -> bool:
    """Verifica se è una vocale, controllando prima se è una stringa."""
    if isinstance(char, str):
        return char.lower() in ["a", "e", "i", "o", "u"]
    raise ValueError("Il valore fornito non è una lettera valida.")

def compute_expected_answer(position: str, char: str, number: int) -> bool:
    """Decide la risposta corretta in base alla posizione della carta."""

    if not isinstance(position, str):
        raise ValueError("La posizione deve essere una parola (stringa).")

    pos = position.lower()
    
    #Se la carta è in alto (TOP), la risposta corretta dipende se il numero è PARI
    if pos == "top":
        return is_even(number)
    #Se la carta è in basso (BOTTOM), la risposta corretta dipende se la lettera è una VOCALE
    elif pos == "bottom":
        return is_vowel(char)
    else:
        raise ValueError(f"Posizione non valida: {position}")