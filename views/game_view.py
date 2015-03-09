import pygame

from base_view import BaseView
from grid_fragment import GridFragment
from grid_sizer import GridSizer
from game_grid_sizer import GameGridSizer
from target_grid_sizer import TargetGridSizer
from measurements import *

class GameView(BaseView):
    BORDER_SIZE = 4
    BORDER_COLOR = pygame.Color("black")

    def __init__(self):
        """ creates the game view """
        self.gameGridFragment = GridFragment()
        self.targetGridFragment = GridFragment()

    def draw(self, puzzleGame):
        surface    = puzzleGame.surface
        gameGrid   = puzzleGame.gameGrid
        targetGrid = puzzleGame.targetGrid
        clicks     = puzzleGame.clicks

        gameGridSizer   = GameGridSizer(surface, gameGrid)
        targetGridSizer = TargetGridSizer(surface, targetGrid)

        self.gameGridFragment.draw(surface, gameGrid, gameGridSizer)
        self.targetGridFragment.draw(surface, targetGrid, targetGridSizer)
        self.drawMenuBar(surface, clicks)
        self.drawBorder(surface)
        pygame.display.update()

    def handleClick(self, puzzleGame, x, y):
        if puzzleGame.clicks == 0:
            return

        rowcol = self.getClickRowCol(puzzleGame, x, y)
        if rowcol:
            puzzleGame.handleGridClick(*rowcol)

    def getClickRowCol(self, puzzleGame, x, y):
        surface  = puzzleGame.surface
        gameGrid = puzzleGame.gameGrid

        gameGridSizer = GameGridSizer(surface, gameGrid)
        return gameGridSizer.getRowCol(x, y)

    def drawMenuBar(self, surface, clicks):
        gridX  = 0
        gridY  = 0
        width  = MENU_BAR_WIDTH_RATIO * surface.get_width()
        height = MENU_BAR_HEIGHT_RATIO * surface.get_height()

        color = pygame.Color("red")
        rect = pygame.rect.Rect(gridX, gridY, width, height)

        surface.fill(color, rect) 
        pygame.draw.rect(surface, self.BORDER_COLOR, rect, self.BORDER_SIZE)

        self.drawMenuBarClicks(surface, clicks)

    def drawBorder(self, surface):
        borderRect = surface.get_rect()
        pygame.draw.rect(surface, self.BORDER_COLOR, borderRect, 2 * self.BORDER_SIZE)

    def drawMenuBarClicks(self, surface, clicks):
        font = pygame.font.SysFont("Arial", 40)
        text = font.render(str(clicks), True, pygame.Color("black"))

        textRect = text.get_rect()
        textRect.centerx = surface.get_rect().centerx
        textRect.bottom = MENU_BAR_HEIGHT_RATIO * surface.get_height()
        surface.blit(text, textRect)
