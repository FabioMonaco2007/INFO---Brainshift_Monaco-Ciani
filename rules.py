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

def calculate_expected_response(position: str, char: str, number: int) -> bool:
    """Decide il controllo usando solo strutture condizionali if/else."""

    if not isinstance(position, str):
        raise ValueError("La posizione deve essere una parola (stringa).")

    pos = position.lower()
    
    if pos == "top":
        return is_even(number)
    elif pos == "bottom":
        return is_vowel(char)
    else:
        raise ValueError(f"Posizione non valida: {position}")
        
