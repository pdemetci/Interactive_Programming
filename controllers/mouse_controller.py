import pygame
from base_controller import BaseController
from game_grid_sizer import GameGridSizer

class MouseController(BaseController):
    
    def __init__(self, puzzleGame):
        """ create the mouse controller """
        self.puzzleGame = puzzleGame

    def handleEvent(self, event):
        """ handles a mouse event """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            surface = self.puzzleGame.surface
            gameGrid = self.puzzleGame.gameGrid
            self.puzzleGame.activeView.handleClick(self, surface, gameGrid, x, y)
           
    def handleGameGridClick(self, x, y):
        if self.puzzleGame.clicks == 0:
            return

        gameGridSizer = GameGridSizer(self.puzzleGame.surface, self.puzzleGame.gameGrid)
        rowcol = gameGridSizer.getRowCol(x, y)
        if rowcol:
            self.puzzleGame.clickHistory.append(rowcol)
            self.puzzleGame.gameGrid.handleGridClick(*rowcol)
            self.puzzleGame.clicks = self.puzzleGame.clicks - 1
            self.puzzleGame.checkWin()

        self.puzzleGame.drawGame()

    def undoGameGridClick(self):
        if not self.puzzleGame.clickHistory:
            return

        lastClick = self.puzzleGame.clickHistory.pop() 
        self.puzzleGame.gameGrid.undoGridClick(*lastClick)
        self.puzzleGame.clicks = self.puzzleGame.clicks + 1

        self.puzzleGame.drawGame()

            
