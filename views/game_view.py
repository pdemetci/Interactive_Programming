import pygame

from base_view import BaseView
from grid_fragment import GridFragment
from draw_game_event import DrawGameEvent
from click_event import ClickEvent
from grid_click_event import GridClickEvent
from get_grid_click_event import GetGridClickEvent
from grid_sizer import GridSizer
from change_cell_event import ChangeCellEvent

class GameView(BaseView):

    def __init__(self):
        """ creates the game view """
        self.gameGridFragment = GridFragment()
        self.targetGridFragment = GridFragment()

    def draw(self, surface, gameGrid, targetGrid):
        """ draw the game grid and target grid """
        gameGridSizer = self.getGameGridSizer(surface, gameGrid)
        targetGridSizer = self.getTargetGridSizer(surface, targetGrid)

        self.gameGridFragment.draw(surface, gameGrid, gameGridSizer)
        self.targetGridFragment.draw(surface, targetGrid, targetGridSizer)

    def notify(self, event):
        nextEvent = None
        if type(event) is DrawGameEvent:
            gameGrid = event.gameGrid
            targetGrid = event.targetGrid
            surface = event.surface

            self.draw(surface, gameGrid, targetGrid)

        elif type(event) is ClickEvent:
            if event.clicksLeft > 0:
                nextEvent = GetGridClickEvent(event.x, event.y)

        elif type(event) is GridClickEvent:
            surface = event.surface
            gameGrid = event.gameGrid
            gameGridSizer = self.getGameGridSizer(surface, gameGrid)

            rowcol = gameGridSizer.getRowCol(event.x, event.y)

            if rowcol:
                row, col = rowcol
                nextEvent = ChangeCellEvent(row, col)

        if nextEvent:
            self.eventManager.post(nextEvent)


    def getGameGridSizer(self, surface, gameGrid):
        """ gets a rectangular portion of the surface """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX = surfaceWidth / 2.0
        gridY = 0
        gridWidth = surfaceWidth / 2.0
        gridHeight = surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return GridSizer(gameGrid.rows, gameGrid.cols, boundsRect)
        
    def getTargetGridSizer(self, surface, targetGrid):
        """ gets a rectangular portion of the surface """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX = 0
        gridY = 0
        gridWidth = surfaceWidth / 2.0
        gridHeight = surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return GridSizer(targetGrid.rows, targetGrid.cols, boundsRect)
        
