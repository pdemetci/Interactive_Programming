import pygame
from base_controller import BaseController

class GameStateController(BaseController):

    def __init__(self, puzzleGame):
        """ create a game state controller """
        self.puzzleGame = puzzleGame
        self.done = True

    def start(self):
        """ start the game """
        self.done = False

    def stop(self):
        """ stop the game """
        self.done = True

    def handleEvent(self, event):
        """ react to QUIT event """
        if event.type == pygame.QUIT:
            self.stop()
