# Architettura

> Qui spiegate **come è fatto dentro** il progetto. Non ripetete il testo della specifica: scrivete cosa avete fatto voi, come lo avete organizzato, e perché.

## Decomposizione in moduli

Abbiamo diviso il progetto in diversi moduli isolati per evitare di avere un unico file gigante ingestibile, distribuendoci meglio i compiti sul repository:

- `main.py`: È il motore del gioco. Contiene il ciclo principale (`while running`), gestisce la tastiera, il timer di sessione, la transizione tra le schermate e coordina i momenti di rendering.
- `models.py`: Contiene solo le strutture dati pure. Abbiamo definito la `dataclass Trial` che mappa le proprietà di ogni carta (lettera, numero, posizione, risposta attesa).
- `rules.py`: Contiene le funzioni logiche per validare la carta (`is_even`, `is_vowel`) e la funzione `compute_expected_answer` che decide la risposta corretta. È un modulo puro.
- `generator.py`: Si occupa di creare un nuovo trial mischiando casualmente i dati tramite l'istanza `random.Random` passata come parametro, assegnando subito la risposta attesa.
- `ui.py`: Contiene la funzione `draw_card`. Serve esclusivamente a disegnare lo shape bianco della carta base quando non ci sono feedback attivi.
- `scoring.py`: Contiene `apply_answer` per calcolare l'aggiunta di punteggio (+10) o la penalità (-5) a ogni risposta data.

## Separazione logica / presentazione

Abbiamo cercato di tenere separata la logica di calcolo da Pygame. I moduli `models.py`, `rules.py`, `generator.py` e `scoring.py` sono moduli "puri": non importano `pygame`. Questo ci permette di testarli in modo isolato usando `pytest`. 
Il rendering grafico e le interazioni avvengono solo in `ui.py` e nel loop principale di `main.py`. Non abbiamo usato variabili globali per lo stato: abbiamo passato i dati esplicitamente alle funzioni (ad esempio l'oggetto `screen` o l'istanza del generatore di numeri casuali `rng`), rendendo il codice molto più pulito e ordinato.

## Macchina a stati

Il gioco si basa su una macchina a due stati controllata all'interno del ciclo principale di `main.py`:

```mermaid
stateDiagram-v2
    [*] --> PLAYING: Avvio del programma
    PLAYING --> RESULTS: Scadono i 60 secondi
    RESULTS --> PLAYING: Pressione del tasto R (Reset)
    PLAYING --> [*]: Pressione del tasto ESC
    RESULTS --> [*]: Pressione del tasto ESC

## Flusso di un trial

Descrivete il ciclo di vita di un singolo trial, dall'istante in cui il generatore lo crea all'istante in cui viene archiviato nelle statistiche. Dove nasce? Come viene valutato? Chi aggiorna lo scoring? Chi attiva il feedback?

Il gioco si basa su una macchina a due stati controllata all'interno del ciclo principale di `main.py`:

```mermaid
stateDiagram-v2
    [*] --> PLAYING: Avvio del programma
    PLAYING --> RESULTS: Scadono i 60 secondi
    RESULTS --> PLAYING: Pressione del tasto R (Reset)
    PLAYING --> [*]: Pressione del tasto ESC
    RESULTS --> [*]: Pressione del tasto ESC

## Dati principali

L'intera sessione si appoggia sulla dataclass Trial definita in models.py:
    -position (str): "TOP" o "BOTTOM".
    -letter (str): Lettera casuale maiuscola (A-Z).
    -number (int): Numero casuale (1-9).
    -expected_answer (bool): Risposta corretta calcolata all'origine dal modulo delle regole.

Nel main.py teniamo traccia dello stato generale tramite variabili locali semplici come score, correct_count, wrong_count,start_time e feedback_until.

## Scoring: come è implementato

Il nostro sistema di scoring risponde alla specifica base tramite la funzione apply_answer in scoring.py. Ad ogni risposta corretta vengono sommati 10 punti. In caso di errore vengono sottratti 5 punti. Il controllo per evitare che il punteggio scenda sotto lo zero è gestito direttamente nel loop principale tramite un'istruzione max(0, ...), mantenendo la funzione di scoring lineare e facilmente testabile.

## Generatore: bilanciamento e seed

La generazione avviene nel modulo generator.py estraendo in modo casuale la posizione, la lettera e il numero tramite l'oggetto rng (un'istanza di random.Random()). Passare l'oggetto rng inizializzato nel main come parametro ci assicura la riproducibilità del comportamento durante i test isolati, permettendoci di controllare che l'estrazione rispetti i vincoli senza creare loop infiniti o dipendenze globali.

## Fading istruzioni

Il meccanismo di scomparsa dei suggerimenti visivi è controllato da una condizione legata alla variabile locale correct_count. All'interno del blocco di rendering dello stato PLAYING, verifichiamo se correct_count < 10. Se la condizione è vera, disegniamo i testi grigi in alto e in basso. Appena l'utente accumula la decima risposta corretta totale, il blocco condizionale diventa falso e i testi smettono di essere disegnati, pulendo completamente l'interfaccia.