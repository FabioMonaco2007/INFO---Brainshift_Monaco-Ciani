# Brain Shift — Progetto di Gruppo

## Chi siamo

- Fabio Monaco — FabioMonaco2007
- Vanessa Ciani — VanessaCiani

Classe 4A Informatica — A.S. 2025-26.

## Cos'è Brain Shift

Brain Shift è un gioco basato sul meccanismo psicologico del *Task Switching*. Lo scopo è rispondere il più velocemente e correttamente possibile a due regole diverse che cambiano continuamente a seconda della posizione in cui compare una carta a schermo. Il gioco mette alla prova la capacità del cervello di passare rapidamente da un compito cognitivo all'altro, penalizzando gli errori e premiando le risposte esatte consecutive.

## Come giocare

Istruzioni per far partire il gioco da clone pulito:

```bash
git clone (https://github.com/FabioMonaco2007/INFO---Brainshift_Monaco-Ciani.git)
cd INFO---Brainshift_Monaco-Ciani
pip install -r requirements.txt
python main.py

Specificate:
- Versione Python richiesta: Python 3.10 o superiore.
- Librerie richieste: pygame (specificata nel file requirements.txt).

## Controlli
- ← Freccia Sinistra: Risposta NO / FALSO
- → Freccia Destra: Risposta SÌ / VERO
- ESC: Esce dal gioco in qualsiasi momento
- R: Ricomincia una nuova partita (attivabile solo nella schermata dei risultati finali)

## Struttura del repository
INFO---Brainshift_Monaco-Ciani/
├── main.py           ← Loop principale, gestione stati e rendering globale
├── models.py         ← Strutture dati pure (dataclass Trial)
├── rules.py          ← Regole logiche del compito cognitivo (Pari, Vocale)
├── generator.py      ← Generazione casuale dei trial e calcolo risposte attese
├── ui.py             ← Funzione di disegno della carta standard
├── scoring.py        ← Calcolo dei punteggi (aggiunta punti e penalità)
├── requirements.txt  ← Dipendenze del progetto (pygame, pytest)
├── docs/             ← Documentazione e diario di bordo (.md)
└── tests/            ← Test automatizzati eseguiti con pytest

## Come lanciare i test
pytest tests/