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

    MENU_BAR_HEIGHT_RATIO    = 0.15
    MENU_BAR_WIDTH_RATIO     = 1
    TARGET_GRID_HEIGHT_RATIO = 1 - MENU_BAR_HEIGHT_RATIO
    TARGET_GRID_WIDTH_RATIO  = 0.5
    GAME_GRID_HEIGHT_RATIO   = 1 - MENU_BAR_HEIGHT_RATIO
    GAME_GRID_WIDTH_RATIO    = 0.5

    def __init__(self):
        """ creates the game view """
        self.gameGridFragment = GridFragment()
        self.targetGridFragment = GridFragment()

    def draw(self, surface, gameGrid, targetGrid, clicks):
        """ draw the game grid and target grid """
        gameGridSizer = self.getGameGridSizer(surface, gameGrid)
        targetGridSizer = self.getTargetGridSizer(surface, targetGrid)

        self.gameGridFragment.draw(surface, gameGrid, gameGridSizer)
        self.targetGridFragment.draw(surface, targetGrid, targetGridSizer)
        self.drawMenuBar(surface, clicks)

    def notify(self, event):
        nextEvent = None
        if type(event) is DrawGameEvent:
            gameGrid = event.gameGrid
            targetGrid = event.targetGrid
            surface = event.surface
            clicks = event.clicks

            self.draw(surface, gameGrid, targetGrid, clicks)

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

    def drawMenuBar(self, surface, clicks):
        gridX  = 0
        gridY  = 0
        width  = self.MENU_BAR_WIDTH_RATIO * surface.get_width()
        height = self.MENU_BAR_HEIGHT_RATIO * surface.get_height()

        color = pygame.Color("red")
        borderColor = pygame.Color("black")
        borderSize = 4
        rect = pygame.rect.Rect(gridX, gridY, width, height)

        surface.fill(color, rect) 
        pygame.draw.rect(surface, borderColor, rect, borderSize)

        pygame.display.update()

    def getGameGridSizer(self, surface, gameGrid):
        """ gets a rectangular portion of the surface """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX      = self.GAME_GRID_WIDTH_RATIO * surfaceWidth
        gridY      = self.MENU_BAR_HEIGHT_RATIO * surfaceHeight
        gridWidth  = self.GAME_GRID_WIDTH_RATIO * surfaceWidth
        gridHeight = self.GAME_GRID_HEIGHT_RATIO * surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return GridSizer(gameGrid.rows, gameGrid.cols, boundsRect)
        
    def getTargetGridSizer(self, surface, targetGrid):
        """ gets a rectangular portion of the surface """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX      = 0
        gridY      = self.MENU_BAR_HEIGHT_RATIO * surfaceHeight
        gridWidth  = self.TARGET_GRID_WIDTH_RATIO * surfaceWidth
        gridHeight = self.TARGET_GRID_HEIGHT_RATIO * surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return GridSizer(targetGrid.rows, targetGrid.cols, boundsRect)
        
