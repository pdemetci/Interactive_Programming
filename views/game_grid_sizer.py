import pygame
from grid_sizer import GridSizer
from measurements import *

class GameGridSizer(GridSizer):
    """ provides dimensions for drawing the game grid """
    
    def __init__(self, surface, gameGrid):
        """ creates a game grid sizer """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX      = GAME_GRID_WIDTH_RATIO * surfaceWidth
        gridY      = MENU_BAR_HEIGHT_RATIO * surfaceHeight
        gridWidth  = GAME_GRID_WIDTH_RATIO * surfaceWidth
        gridHeight = GAME_GRID_HEIGHT_RATIO * surfaceHeight
        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)

        super(GameGridSizer, self).__init__(gameGrid.rows, gameGrid.cols, boundsRect)
 

