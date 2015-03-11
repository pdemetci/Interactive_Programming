import pygame
from base_controller import BaseController

class GameStateController(BaseController):

    def __init__(self, puzzleGame):
        """ create a game state controller """
        self.puzzleGame = puzzleGame
        self.done = True

    def start(self):
        self.done = False

    def stop(self):
        self.done = True

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            self.stop()
