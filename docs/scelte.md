# Scelte implementative

> Qui va la parte più **metacognitiva** del progetto: cosa avete scelto, perché, cosa avete scartato. Non può essere scritta dall'IA — è il ragionamento che mostra che avete capito quello che avete fatto.

## Scelte rilevanti

### 1. Rappresentazione dei dati con una Dataclass pura
- **Cosa**: Abbiamo scelto di usare la `dataclass Trial` in `models.py` per salvare tutte le informazioni relative a una singola carta.
- **Perché**: Evita di dover passare dizionari o tuple anonime tra i moduli, garantendo che i campi (`letter`, `number`, `position`, `expected_answer`) siano fissi e documentati.
- **Alternative considerate**: Usare un dizionario standard (`dict`). Scartato perché espone al rischio di errori di battitura nelle chiavi (es. scrivere `"pos"` al posto di `"position"`) difficili da intercettare subito.
- **Conseguenze**: Il passaggio di dati tra `generator.py`, `ui.py` e `main.py` è diventato rigidamente tipizzato e molto pulito.

### 2. Gestione del tempo tramite modulo standard `time`
- **Cosa**: Abbiamo usato `time.time()` sia per gestire la durata della sessione (i 60 secondi), sia per calcolare la scadenza del feedback visivo.
- **Perché**: Fornisce timestamp precisi in secondi (con decimali per i millisecondi) indipendenti dal frame-rate effettivo di Pygame.
- **Alternative considerate**: Utilizzare `pygame.time.get_ticks()`. Scartata perché volevamo che la logica temporale principale non fosse strettamente legata alle funzioni di Pygame, facilitando calcoli lineari basati sul tempo reale di sistema.
- **Conseguenze**: Il calcolo del countdown e della finestra di feedback di 150ms avviene tramite semplici sottrazioni matematiche nel loop principale, senza appesantire la macchina.

### 3. Feedback visivo non bloccante tramite cache del trial precedente
- **Cosa**: Quando l'utente risponde, salviamo il trial corrente in una variabile di appoggio `feedback_trial`, generiamo subito la nuova carta in background e attiviamo un timer di 150ms per colorare la vecchia posizione.
- **Perché**: Se avessimo usato un blocco hardware come `time.sleep(0.150)`, avremmo congelato l'intera finestra di gioco, bloccando il refresh dello schermo e la chiusura della finestra.
- **Alternative considerate**: Utilizzare un sistema a frame o congelare il loop. Scartata perché l'interfaccia sarebbe risultata scattante e poco fluida.
- **Conseguenze**: Il loop gira fluidamente a 60 FPS stabili. L'utente vede la vecchia carta colorarsi di verde o rosso pastello per 150ms, mentre la nuova carta è già pronta in memoria per apparire subito dopo.

### 4. Palette grafiche pastello e sfondo scuro (Polish finali)
- **Cosa**: Abbiamo sostituito lo sfondo nero puro e i colori RGB saturi con uno sfondo grigio scuro `(30, 30, 30)` e tonalità pastello per il feedback (`SeaGreen` per il corretto e `FireBrick` per l'errore).
- **Perché**: I colori primari puri sparati a schermo intero stancavano gli occhi durante le sessioni di test e davano al gioco un aspetto amatoriale.
- **Alternative considerate**: Mantenere i colori base `(0, 255, 0)` e `(255, 0, 0)`. Scartata per ragioni di resa estetica e usabilità visiva.
- **Conseguenze**: L'applicazione risulta visivamente più rifinita e l'interfaccia è più leggibile grazie alla centratura automatica basata sulle coordinate dello schermo.

## Cosa non siamo riusciti a fare e perché

- **1:**: Ci siamo limitati a fare "solamente" i requisiti minimi principalmente per mancanza di tempo, essendo che abbiamo dedicato molto tempo nel cercare di fare le cose in modo super ordinato per non perderci nulla e non confonderci tra i vari file e cartelle presenti.
- **2:**: Inoltre ci sarebbe piaciuto rendere la schermata di gioco un po' più carina da vedere e non lasciarla cosi "minimal". Ma anche qui per mancanza di tempo, e anche per alcune nostre mancanze, non siamo stati in grado di farlo.