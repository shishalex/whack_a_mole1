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