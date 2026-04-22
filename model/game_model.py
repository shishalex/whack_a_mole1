from random import randint

class Hole:
    """Un singolo buco della griglia."""

    def __init__(self, hole_index: None|int):
        self.is_active = False
        self.hole_index = None

    def toggle_active(self):
        self.is_active = not self.is_active


class GameModel:
    """Stato complessivo del gioco."""

    NUM_HOLES = 9

    def __init__(self):
        self.holes = [Hole(i) for i in range(self.NUM_HOLES)]

    def toggle_hole(self, index: int):
        if 0 <= index < self.NUM_HOLES:
            self.holes[index].toggle_active()
        else:
            raise IndexError("Indice non valido per i buchi")
