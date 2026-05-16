# Uso dell'IA nel progetto

> Questa pagina serve a dichiarare **in modo onesto e granulare** come avete usato assistenti IA (ChatGPT, Claude, Copilot, Gemini, ecc.) durante lo sviluppo. È obbligatoria. Va scritta **da voi**, non dall'IA.

---

## Politica del progetto

L'IA è consentita come assistente (spiegazioni, suggerimenti, debug, codice di dettaglio ben compreso) ma non come risolutore automatico (generazione e consegna di codice non compreso). Le parti di **documentazione e metacognizione** (questa pagina inclusa, `devlog.md`, `scelte.md`) vanno scritte senza IA.

---

## Strumenti usati

Elencate gli strumenti IA che il gruppo ha effettivamente usato durante il progetto:

- [ ] Gemini (Modello: Advanced) — Utilizzato per il debug della logica temporale non bloccante, suggerimenti sulla palette di colori da utilizzare e cosigli generali su alcuni piccoli problemi di coding riscontrati durante l'implementazione.

## Uso granulare per modulo / parte

### Parte 1
* **Dove**: `main.py`, gestione del feedback visivo nel blocco eventi e rendering.
* **Cosa abbiamo chiesto**: Come far colorare di verde o rosso la carta appena risposta per 150ms senza usare `time.sleep()`, dato che quest'ultimo congelava l'intera finestra di Pygame.
* **Cosa ci ha suggerito**: Ci ha suggerito di salvare lo stato della carta precedente in una variabile di appoggio (cache) prima di generare il nuovo trial, impostando un timestamp futuro (`time.time() + 0.15`). Nel rendering, finché il tempo corrente è minore del timestamp, disegniamo manualmente il rettangolo colorato basandoci sulla carta vecchia.
* **Cosa abbiamo fatto**: Abbiamo integrato perfettamente la logica modificando il nostro ciclo di eventi in `main.py` e introducendo la variabile `feedback_trial`. Questo ha risolto il bug visivo mantenendo il gioco fluido e rispondente a 60 FPS.

### Parte 2
* **Dove**: `main.py`, blocco di rendering e configurazione grafica.
* **Cosa abbiamo chiesto**: Come allineare in modo pulito e centrato i testi della schermata dei risultati e del timer, e quali valori RGB usare per evitare colori primari troppo accesi.
* **Cosa ci ha suggerito**: Ci ha fornito le formule matematiche basate su `screen_width // 2 - text.get_width() // 2` per calcolare l'offset esatto di blit e ci ha proposto una palette di colori "pastello" (`SeaGreen`, `FireBrick` e uno sfondo grigio scuro `30, 30, 30`).
* **Cosa abbiamo fatto**: Abbiamo applicato le modifiche alle coordinate del testo e aggiornato i codici RGB delle tuple nel codice, ottenendo un'interfaccia simmetrica e molto più gradevole da vedere.

## Cosa non abbiamo chiesto all'IA

Le seguenti parti sono state progettate, scritte e collaudate interamente da noi senza alcun supporto esterno:
* La separazione in moduli del progetto e la struttura della dataclass `Trial` in `models.py`.
* La logica pura di controllo delle regole (`is_even`, `is_vowel` e `compute_expected_answer`) in `rules.py`.
* La logica di incremento e decremento del punteggio bloccato a zero in `scoring.py`.
* Tutti i diari di bordo, l'architettura e le riflessioni contenute in questi file di documentazione.