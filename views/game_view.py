import pygame

from base_view import BaseView
from grid_fragment import GridFragment
from grid_sizer import GridSizer
from target_grid_sizer import TargetGridSizer
from game_grid_sizer import GameGridSizer
from measurements import *

class GameView(BaseView):
    BORDER_SIZE = 4
    BORDER_COLOR = pygame.Color("black")

    def __init__(self):
        """ creates the game view """
        self.gameGridFragment = GridFragment()
        self.targetGridFragment = GridFragment()

    def handleClick(self, controller, puzzleGame, x, y):
        """ react to a click """
        surface = puzzleGame.surface
        gameGrid = puzzleGame.gameGrid
        if self.clickedUndo(surface, x, y):
            controller.undoGameGridClick()
        elif self.clickedGameGrid(surface, gameGrid, x, y):
            controller.handleGameGridClick(x, y)
            
    def clickedUndo(self, surface, x, y):
        """ check if the undo button was clicked """
        undoButtonRect = self.getUndoButtonRect(surface)
        return undoButtonRect.collidepoint(x, y)

    def clickedGameGrid(self, surface, gameGrid, x, y):
        """ check if the game grid was clicked """
        gameGridRect = self.getGameGridRect(surface, gameGrid)
        return gameGridRect.collidepoint(x, y)

    def draw(self, puzzleGame):
        """ draw the game """
        surface    = puzzleGame.surface
        gameGrid   = puzzleGame.gameGrid
        targetGrid = puzzleGame.targetGrid
        clicks     = puzzleGame.clicks

        gameGridSizer   = GameGridSizer(surface, gameGrid)
        targetGridSizer = TargetGridSizer(surface, targetGrid)

        self.gameGridFragment.draw(surface, gameGrid, gameGridSizer)
        self.targetGridFragment.draw(surface, targetGrid, targetGridSizer)
        self.drawMenuBar(surface, clicks)
        self.drawDivider(surface)
        self.drawBorder(surface)
        
        pygame.display.update()

    def drawDivider(self, surface):
        """ draw the divider between grids """
        x0 = TARGET_GRID_WIDTH_RATIO * surface.get_width()
        x1 = x0
        y0 = MENU_BAR_HEIGHT_RATIO * surface.get_height()
        y1 = surface.get_height()
        width = 8

        startPos = (x0, y0)
        endPos = (x1, y1)

        color = pygame.Color("grey")

        pygame.draw.line(surface, color, startPos, endPos, width)

    def drawMenuBar(self, surface, clicks):
        """ draw the top bar """
        self.drawMenuBarBackground(surface)
        self.drawMenuBarClicks(surface, clicks)
        self.drawMenuBarUndoButton(surface)

    def drawMenuBarBackground(self, surface):
        """ draw the top bar background """
        gridX  = 0
        gridY  = 0
        width  = MENU_BAR_WIDTH_RATIO * surface.get_width()
        height = MENU_BAR_HEIGHT_RATIO * surface.get_height()

        color = pygame.Color("red")
        rect = pygame.rect.Rect(gridX, gridY, width, height)

        surface.fill(color, rect) 
        pygame.draw.rect(surface, self.BORDER_COLOR, rect, self.BORDER_SIZE)

    def getFont(self):
        """ get the writing font """
        font = pygame.font.SysFont("Arial", 40)
        return font
        
    def getUndoText(self):
        """ get the undo text """
        font = self.getFont()
        text = font.render("undo", True, pygame.Color("black"))
        return text

    def drawMenuBarUndoButton(self, surface):
        """ draw the undo button """
        text = self.getUndoText()
        undoTextRect = self.getUndoTextRect(surface)
        undoButtonRect = self.getUndoButtonRect(surface)
        surface.fill(pygame.Color("purple"), undoButtonRect)
        surface.blit(text, undoTextRect)

    def getUndoTextRect(self, surface):
        """ get the undo text rectangle """
        font = self.getFont()
        text = self.getUndoText()

        textRect = text.get_rect()
        textRect.centery = 0.5 * MENU_BAR_HEIGHT_RATIO * surface.get_height()
        textRect.right = 0.98 * MENU_BAR_WIDTH_RATIO * surface.get_width()
        return textRect

    def getUndoButtonRect(self, surface):
        """ get the undo button rectangle """
        textRect = self.getUndoTextRect(surface)
        undoRect = textRect.inflate(10, 6)
        return undoRect

    def getGameGridRect(self, surface, gameGrid):
        """ get the game grid rectangle """
        gameGridSizer = GameGridSizer(surface, gameGrid)
        return gameGridSizer.getGridRect()

    def drawMenuBarClicks(self, surface, clicks):
        """ write the number of clicks left """
        font = self.getFont()
        text = font.render(str(clicks), True, pygame.Color("black"))

        textRect = text.get_rect()
        textRect.centerx = surface.get_rect().centerx
        textRect.centery = 0.5 * MENU_BAR_HEIGHT_RATIO * surface.get_height()
        surface.blit(text, textRect)

    def drawBorder(self, surface):
        """ draw the view's  border """
        borderRect = surface.get_rect()
        pygame.draw.rect(surface, self.BORDER_COLOR, borderRect, 2 * self.BORDER_SIZE)

