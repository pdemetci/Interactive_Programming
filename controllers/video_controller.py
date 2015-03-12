import pygame
from base_controller import BaseController

class VideoController(BaseController):
    
    def __init__(self, puzzleGame):
        """ create the video controller """
        self.puzzleGame = puzzleGame

    def handleEvent(self, event):
        """ react to VIDEORESIZE event """
        if event.type == pygame.VIDEORESIZE:
            wh = event.w, event.h
            self.puzzleGame.surface = pygame.display.set_mode(wh, pygame.RESIZABLE)
            self.puzzleGame.drawGame()
