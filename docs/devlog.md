# Devlog — Brainshift

> Diario di bordo del gruppo. Una entry alla settimana (minimo tre, una per settimana di lavoro). Scritto **da voi**, non dall'IA.

---

## Cos'è un devlog e come si scrive

Un *devlog* (development log) è un diario tecnico del progetto. Serve a:

- **Voi**: obbligarvi a riflettere su quello che si sta facendo, su come procede, su cosa non funziona. Tenere traccia delle decisioni prese, così a due settimane di distanza ci si ricorda perché si era scelto qualcosa.
- **Al docente**: vedere che tipo di processo di sviluppo avete portato avanti, come avete reagito agli ostacoli, come si è distribuito il lavoro nel tempo.

Non è un registro formale («oggi ho fatto X, Y, Z»), ma nemmeno un tema. È **tecnico e onesto**: cosa avete fatto, cosa avete capito, cosa non avete capito, cosa vi ha fatto perdere tempo, cosa avete deciso.

### Regole pratiche

- **Frequenza**: almeno una entry a settimana. Meglio due. Senza passare settimane in silenzio.
- **Lunghezza**: 15-30 righe a entry. Non serve di più. Non accettate entry di due righe tipo «questa settimana abbiamo fatto lo scoring».
- **Stile**: prima persona plurale (siete un gruppo). Linguaggio normale, frasi dirette. Niente «abbiamo proceduto alla realizzazione di»: scrivete «abbiamo scritto».
- **Onestà**: se una settimana non avete fatto nulla, scrivetelo. Se avete litigato su qualcosa, dite su cosa (senza attaccare nessuno). Se vi siete bloccati tre giorni su un bug, raccontate il bug.

### Cosa mettere in ogni entry

Linee guida, non obbligatorie in modo rigido. Ogni entry dovrebbe toccare almeno tre di questi punti:

- **cosa abbiamo fatto questa settimana** (fatti, non aspirazioni)
- **cosa ci ha fatto perdere tempo** e perché
- **cosa abbiamo imparato di nuovo** (tecnicamente o organizzativamente)
- **decisioni prese** questa settimana: cosa abbiamo scelto, perché, cosa abbiamo scartato
- **cosa pianifichiamo per la settimana prossima**
- **divisione del lavoro**: chi sta facendo cosa in questo momento

---

## Entry

### Settimana 1 (22-28 aprile 2026)

Nella prima settimana ci siamo concentrati sull'architettura iniziale del progetto. Abbiamo deciso di dividerci i moduli fin da subito per lavorare in parallelo su GitHub. Abbiamo definito la finestra principale di Pygame a 800x600 e creato il file `models.py` con la dataclass per il `Trial`. Abbiamo implementato la logica in `rules.py` per stabilire se un numero è pari o se una lettera è una vocale, con la funzione `compute_expected_answer` per calcolare la risposta corretta a seconda della posizione della carta.

### Settimana 2 (29 aprile - 5 maggio 2026)

Questa settimana abbiamo sviluppato l'interfaccia di base e la cattura dell'input. Abbiamo creato il modulo `ui.py` con la funzione `draw_card` per visualizzare graficamente la carta a schermo, posizionandola in alto (Y=100) o in basso (Y=350) e centrandola orizzontalmente. Successivamente abbiamo mappato i controlli da tastiera nel `main.py` legando le Frecce Destra e Sinistra rispettivamente a SÌ e NO. Infine, abbiamo implementato il modulo `scoring.py` applicando i punteggi (+10 per risposte corrette, -5 per gli errori) e bloccando il valore minimo a zero per evitare punteggi negativi.

### Settimana 3 (6-12 maggio 2026)

Ci siamo dedicati alla gestione del tempo e alla macchina a stati. Abbiamo aggiunto una variabile di stato per scambiare la schermata di gioco attivo (`PLAYING`) con la schermata dei risultati finali (`RESULTS`). Usando il modulo `time`, abbiamo inserito un timer di sessione non bloccante di 60 secondi con un conto alla rovescia visibile. Nella schermata finale abbiamo inserito il riepilogo dei punti accumulati, delle risposte giuste/sbagliate e il calcolo della percentuale di accuratezza. Abbiamo anche aggiunto il tasto `R` per resettare la partita e rigiocare senza dover riavviare lo script.

### Settimana finale (13-17 maggio 2026)

Nell'ultima settimana abbiamo chiuso i requisiti avanzati e rifinito l'esperienza utente. Abbiamo riscontrato un bug iniziale nel feedback visivo: la nuova carta si colorava anziché quella appena data. Abbiamo risolto inserendo una variabile di cache `feedback_trial` che salva temporaneamente il vecchio trial per mostrarlo colorato di verde o rosso per 150ms senza congelare il gioco con dei `sleep`. Abbiamo inserito le istruzioni testuali grigie in alto e in basso e implementato il meccanismo di fading che le nasconde non appena il giocatore raggiunge 10 risposte corrette. Infine, abbiamo fatto un restyling grafico con colori più morbidi e centrato tutti i testi geometricamente.

## Bilancio finale

In conclusione, siamo davvero molto soddisfatti di come siamo riusciti a lavorare in coppia. Fin dall'inizio siamo stati capaci di dividerci i compiti in modo equo, un aspetto che si vede chiaramente anche nella cronologia dei commit su GitHub. La collaborazione è stata efficiente: ci siamo aiutati a vicenda ogni volta che si presentava un problema, scambiandoci consigli e idee sia sulla logica dei moduli sia sulle scelte di programmazione.
Siamo molto fieri della stabilità del gioco finale e di come risponda a tutti i requisiti.
Anche se il risultato ci soddisfa molto, se avessimo avuto un altro po' di tempo ci sarebbe piaciuto migliorare ulteriormente la grafica principale del gioco. Pur avendo rifinito l'impatto visivo con la palette pastello e lo sfondo scuro, ci sarebbe piaciuto aggiungere delle animazioni fluide per lo scorrimento delle carte e qualche effetto sonoro per rendere il gioco ancora più interattivo.
Noi pensiamo e ci auguriamo che questo progetto possa permetterci di arrivare ad un punteggio positivo: la logica è solida, il codice è pulito, i test con pytest passano tutti e le specifiche sono state rispettate rigorosamente; manca solo un briciolo di rifinitura estetica avanzata per definirlo perfetto. Ci auguriamo che l'impegno costante e la qualità del codice finale vengano ripagate.