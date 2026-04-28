from dataclasses import dataclass

#Una dataclass è un modo rapido per creare una classe che serve solo a contenere dati. 
@dataclass
class Trial:
    user_answer: bool | None = None
    is_correct: bool = False