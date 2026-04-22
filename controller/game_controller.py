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
    SCREEN_W = 800
    SCREEN_H = 600
    FPS = 60

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        pygame.display.set_caption("Acchiappa la talpa!")
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__handle_click(event.pos)
            self.view.draw(self.model)
            self.clock.tick(self.FPS)


    def __handle_click(self, pos):
        hole_index = self.__hole_at(pos)
        if hole_index is not None:
            self.model.toggle_hole(hole_index)


    def __hole_at(self, pos):
        for hole in  self.model.holes:
            cx, cy = hole_center(hole.hole_index)
            dx = pos[0] - cx
            dy = pos[1] - cy
            distance = math.hypot(dx, dy)
            if distance <= HOLE_RADIUS:
                return hole.hole_index
        return None