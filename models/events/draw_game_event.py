from base_event import BaseEvent

class DrawGameEvent(BaseEvent):

    def __init__(self, surface, gameGrid, targetGrid):
        self.surface = surface
        self.gameGrid = gameGrid
        self.targetGrid = targetGrid
