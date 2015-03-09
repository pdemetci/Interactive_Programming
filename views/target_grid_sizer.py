import pygame
from grid_sizer import GridSizer
from measurements import *

class TargetGridSizer(GridSizer):
    """ provides dimensions for drawing the target grid """
    
    def __init__(self, surface, gameGrid):
        """ creates a game grid sizer """
        surfaceWidth, surfaceHeight = surface.get_size()

        gridX      = 0
        gridY      = MENU_BAR_HEIGHT_RATIO * surfaceHeight
        gridWidth  = TARGET_GRID_WIDTH_RATIO * surfaceWidth
        gridHeight = TARGET_GRID_HEIGHT_RATIO * surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        super(TargetGridSizer, self).__init__(gameGrid.rows, gameGrid.cols, boundsRect)
 

