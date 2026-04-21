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