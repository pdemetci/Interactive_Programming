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
            self.puzzleGame.activeView.handleClick(self, self.puzzleGame, x, y)
           
    def handleGameGridClick(self, x, y):
        """ handle clicks that occur in the GameGrid """

        # do nothing if there are not clicks left
        if self.puzzleGame.clicks == 0:
            return

        # get the (row, col) location of the click
        gameGridSizer = GameGridSizer(self.puzzleGame.surface, self.puzzleGame.gameGrid)
        rowcol = gameGridSizer.getRowCol(x, y)

        # if in bounds, react to the click
        if rowcol:
            self.puzzleGame.clickHistory.append(rowcol)
            self.puzzleGame.gameGrid.handleGridClick(*rowcol)
            self.puzzleGame.clicks = self.puzzleGame.clicks - 1
            self.puzzleGame.drawGame()
            self.puzzleGame.checkWin()
        else:
            self.puzzleGame.drawGame()

    def undoGameGridClick(self):
        """ undo a grid click """

        # check if there have been previous clicks
        if not self.puzzleGame.clickHistory:
            return

        # get the last click position and undo it
        lastClick = self.puzzleGame.clickHistory.pop() 
        self.puzzleGame.gameGrid.undoGridClick(*lastClick)
        self.puzzleGame.clicks = self.puzzleGame.clicks + 1

        self.puzzleGame.drawGame()

            
