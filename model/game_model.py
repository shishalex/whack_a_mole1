from random import randint

class Hole:
    """Un singolo buco della griglia."""
    # TODO: definire un costruttore che inizializzi lo stato (is_active) a False
    # TODO: definire un metodo 'toggle' per invertire lo stato (is_active)

    def __init__(self,x: int, y: int):
        self.__is_active = False

    def toggle_active(self):
        self.__is_active = not self.__is_active


class GameModel:
    """Stato complessivo del gioco."""
    # TODO: definire un costruttore che inizializzi una lista di 'NUM_HOLES' buchi
    # TODO: definire un metodo 'toggle_hole(index)' per invocare il toggle del buco corrispondente (con validazione)

    NUM_HOLES = 9

    def __init__(self):
        self.__holes = []
        for _ in range(self.NUM_HOLES):
            self.__holes.append(Hole())

    def toggle_hole(self, index: int):
        if 0 <= index < self.NUM_HOLES:
            self.__holes[index].toggle_active()
        else:
            raise IndexError("Indice non valido per i buchi")
