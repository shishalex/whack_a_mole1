# Whack-a-Mole — Step 1

## 1. Obiettivi

In questo primo step costruirai lo scheletro del gioco senza ancora implementare la meccanica vera e propria. Al termine sarai in grado di aprire una finestra Pygame, disegnare una griglia 3×3 di cerchi sullo schermo, gestire il clic del mouse per individuare quale cerchio è stato premuto e organizzare il codice secondo il pattern *MVC* fin dalle prime righe.

L'idea guida è semplice: prima la struttura, poi il gioco. Avere model, view e controller già separati renderà naturale, negli step successivi, aggiungere talpe, tempo e punteggio senza dover riscrivere nulla.

## 2. Cosa otterrai alla fine

Una finestra con nove cerchi grigi disposti su tre righe e tre colonne. Cliccando su un cerchio, questo cambia colore — diventa, ad esempio, arancione — e ci resta. Cliccandoci sopra una seconda volta torna grigio. Cliccando fuori dai cerchi non succede nulla. Chiudendo la finestra il programma termina in modo pulito.

Nessun punteggio, nessun timer, nessuna talpa: solo una griglia che reagisce al mouse. È poco, ma è già un'applicazione MVC funzionante.

## 3. Struttura del progetto

Crea le cartelle e i file seguenti. I file possono inizialmente essere vuoti: li riempirai man mano.

```
whack_a_mole/
├── main.py
├── model/
│   └── game_model.py
├── view/
│   └── game_view.py
└── controller/
    └── game_controller.py
```

> **📌 Ricorda: il pattern MVC**
>
> - **Model** — contiene i dati e la logica. Non importa mai `pygame`.
> - **View** — disegna sullo schermo. Legge i dati dal model, non li modifica.
> - **Controller** — riceve gli eventi, aggiorna il model, chiede alla view di ridisegnarsi.

In questo step il model conterrà soltanto lo stato dei nove buchi (attivo o inattivo), la view saprà disegnarli e il controller gestirà il loop principale e i clic del mouse.

## 4. Il model

Apri `model/game_model.py` e definisci due classi: `Hole`, che rappresenta un singolo buco, e `GameModel`, che ne contiene nove.

```python
class Hole:
    """Un singolo buco della griglia."""
    # TODO: definire un costruttore che inizializzi lo stato (is_active) a False
    # TODO: definire un metodo 'toggle' per invertire lo stato (is_active)


class GameModel:
    """Stato complessivo del gioco."""
    NUM_HOLES = 9

    # TODO: definire un costruttore che inizializzi una lista di 'NUM_HOLES' buchi
    # TODO: definire un metodo 'toggle_hole(index)' per invocare il toggle del buco corrispondente (con validazione)

```

Nota che in questo file non compare nessun riferimento a Pygame. Questa è la regola d'oro del model: deve poter essere testato — anche da riga di comando — senza bisogno di aprire una finestra grafica.

> **Domanda.** Perché conviene rappresentare i buchi come una lista lineare di nove elementi invece che come una matrice 3×3?

## 5. La view

Apri `view/game_view.py`. Qui definirai costanti grafiche, una funzione che converte indice di griglia in coordinate pixel e una classe `GameView` che disegna tutto.

```python
import pygame

# Dimensioni finestra
WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 600

# Griglia
GRID_ROWS    = 3
GRID_COLS    = 3
HOLE_RADIUS  = 60
GRID_MARGIN  = 60

# Colori
COLOR_BG       = (30, 30, 40)
COLOR_HOLE     = (90, 90, 100)
COLOR_HOLE_ON  = (230, 140, 40)


def hole_center(index):
    """Restituisce le coordinate (x, y) del centro del buco i-esimo."""
    # TODO: calcolare la riga e la colonna corrispondenti all'indice
    # TODO: calcolare le dimensioni di una singola cella (larghezza e altezza) escludendo i margini
    # TODO: calcolare e restituire le coordinate del centro (cx, cy) per il buco
    pass


class GameView:
    # TODO: definire costruttore __init__(self, screen) che memorizzi la superficie 'screen'

    # TODO: definire un metodo 'draw(self, model)' che:
    #       - riempie lo schermo con il colore di sfondo COLOR_BG
    #       - disegna un cerchio per ogni buco usando il colore appropriato in base allo stato
    #       - aggiorna la finestra di display (pygame.display.flip())
    pass
```

Osserva due cose. Primo, `draw()` riceve il `model` come parametro: la view legge lo stato ma non lo modifica mai. Secondo, `hole_center()` è una funzione pura — date le costanti, restituisce sempre lo stesso risultato per lo stesso indice — quindi è facile da testare e da riusare anche nel controller per capire su quale buco è avvenuto un clic.

> **Domanda.** Se cambiassi `WINDOW_WIDTH` a 800, cosa succederebbe alla disposizione dei buchi? Devi modificare anche `hole_center()`?

## 6. Il controller

Apri `controller/game_controller.py`. Il controller possiede il model e la view, gestisce il loop principale e traduce gli eventi del mouse in chiamate al model.

```python
import math
import pygame

from model.game_model import GameModel
from view.game_view import GameView, hole_center, HOLE_RADIUS, WINDOW_WIDTH, WINDOW_HEIGHT


class GameController:
    # TODO: definire costruttore __init__(self) che inizializzi pygame, lo schermo, il clock, model e view

    # TODO: definire metodo 'run(self)' con il loop principale del gioco:
    #       - gestire l'evento QUIT per uscire
    #       - gestire MOUSEBUTTONDOWN per catturare il clic (invocando _handle_click)
    #       - chiamare view.draw e impostare il framerate a 60

    # TODO: definire metodo '_handle_click(self, pos)' che trova l'indice cliccato e lo inverte nel model

    # TODO: definire metodo '_hole_at(self, pos)' che:
    #       - calcola la distanza tra la posizione e i centri dei buchi
    #       - restituisce l'indice del buco se ci troviamo all'interno del suo raggio, altrimenti None
    pass
```

Il metodo `_hole_at()` merita attenzione. Per capire se un punto si trova dentro un cerchio si usa la distanza euclidea tra il punto e il centro: se è minore o uguale al raggio, il clic è avvenuto sul buco. La funzione `math.hypot(dx, dy)` calcola esattamente $\sqrt{dx^2 + dy^2}$ in modo numericamente stabile.

> **Domanda.** Perché controlliamo `event.type == MOUSEBUTTONDOWN` invece di leggere `pygame.mouse.get_pressed()` a ogni frame? Cosa cambierebbe nel comportamento del gioco?

## 7. Il punto di ingresso

Apri `main.py` nella cartella radice e scrivi:

```python
from controller.game_controller import GameController

if __name__ == "__main__":
    GameController().run()
```

Tutto qui. Il punto di ingresso non sa nulla di Pygame: si limita a istanziare il controller e a chiamare `run()`. Se un domani volessi sostituire l'interfaccia grafica con qualcos'altro, dovresti toccare solo la view e il controller.

## 8. Come avviare

Dalla cartella radice del progetto:

```bash
pip install pygame
python main.py
```

Dovresti vedere una finestra 600×600 con nove cerchi grigi. Cliccandoci sopra cambiano colore.

## 9. Cosa devi fare tu

Il codice di questo step è quasi tutto guidato: l'obiettivo è scriverlo, capirlo e farlo funzionare. Ecco i compiti concreti:

- ricrea la struttura di cartelle e scrivi il codice nei file corrispondenti;
- assicurati che il gioco si avvii e che i clic funzionino;
- rispondi per iscritto, in un commento all'inizio di `main.py`, alle tre domande poste nelle sezioni precedenti;
- modifica `GRID_ROWS` e `GRID_COLS` a 4 e verifica che la griglia diventi 4×4 senza altre modifiche al codice. Se qualcosa si rompe, capisci perché e correggi.

L'ultimo punto è il più importante: serve a testare se la separazione delle responsabilità che abbiamo introdotto regge davvero. Una buona architettura si misura dalla facilità con cui si possono fare piccoli cambiamenti senza effetti collaterali.

## 10. Anticipazione del prossimo step

Nello step 2 trasformeremo questa griglia statica in un gioco vero. Le talpe inizieranno a comparire da sole in buchi casuali, resteranno visibili per qualche secondo e poi spariranno. Avrai un timer di partita, un punteggio e un conteggio dei mancati. La struttura MVC che hai costruito ora ti permetterà di aggiungere tutto questo toccando soprattutto il model — la view e il controller cambieranno poco.
