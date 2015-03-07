from base_event import BaseEvent

class GridClickEvent(BaseEvent):

    def __init__(self, surface, gameGrid, x, y):
        self.surface = surface
        self.gameGrid = gameGrid
        self.x = x
        self.y = y
