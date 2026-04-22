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

    row = index // GRID_ROWS
    col = index % GRID_COLS

    width = WINDOW_WIDTH - 2 * GRID_MARGIN
    height = WINDOW_HEIGHT - 2 * GRID_MARGIN
    cell_width = width / GRID_ROWS
    cell_height = height / GRID_COLS

    cx = int(GRID_MARGIN + col * cell_width + cell_width / 2)
    cy = int(GRID_MARGIN + row * cell_height + cell_height / 2)

    return cx, cy


class GameView:
    # TODO: definire costruttore __init__(self, screen) che memorizzi la superficie 'screen'

    # TODO: definire un metodo 'draw(self, model)' che:
    #       - riempie lo schermo con il colore di sfondo COLOR_BG
    #       - disegna un cerchio per ogni buco usando il colore appropriato in base allo stato
    #       - aggiorna la finestra di display (pygame.display.flip())
    def __init__(self, screen):
        self.__screen = screen

    def draw(self, model):
        self.__screen.fill(COLOR_BG)
        for hole in model.holes:
            if hole.is_active:
                color = COLOR_HOLE_ON
            else:
                color = COLOR_HOLE
            cx, cy = hole_center(hole.hole_index)
            pygame.draw.circle(self.screen, color, (cx, cy), HOLE_RADIUS)
        pygame.display.flip()