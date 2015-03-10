import pygame

from game_grid import GameGrid
from target_grid import TargetGrid
from game_view import GameView
from menu_view import MenuView
from game_grid_sizer import GameGridSizer

class PuzzleGame:
    GAME_WIDTH = 1200
    GAME_HEIGHT = 720

    ROWS = 5
    COLS = 5

    MAX_CLICKS = 10

    def __init__(self):
        """ create the view and controllers """
        self.done = True

        self.gameGrid = GameGrid(self.ROWS, self.COLS)
        self.targetGrid = TargetGrid(self.ROWS, self.COLS, 1)
        self.clicks = self.MAX_CLICKS
        self.clickHistory = []

        self.gameView = GameView()
        self.menuView = MenuView()
        self.activeView = None
        self.surface = None

    def start(self):
        """ start the game """
        self.done = False
        self.switchView(self.gameView)
        self.surface = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT), pygame.RESIZABLE)
        self.drawGame()

        while not self.done:
            self.main()
            pygame.time.wait(50)

    def stop(self):
        """ stop the game """
        self.done = True

    def main(self):
        """ body of the main loop """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.handleClick(x, y)
            elif event.type == pygame.VIDEORESIZE:
                width = event.w
                height = event.h
                self.surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                self.drawGame()

    def drawGame(self):
        self.activeView.draw(self)

    def handleClick(self, x, y):
        self.activeView.handleClick(self, x, y)

    def handleGameGridClick(self, x, y):
        if self.clicks == 0:
            return

        gameGridSizer = GameGridSizer(self.surface, self.gameGrid)
        rowcol = gameGridSizer.getRowCol(x, y)
        if rowcol:
            self.clickHistory.append(rowcol)
            self.gameGrid.handleGridClick(*rowcol)
            self.clicks = self.clicks - 1
            self.checkWin()

        self.drawGame()

    def undoGameGridClick(self):
        if not self.clickHistory:
            return

        lastClick = self.clickHistory.pop() 
        self.gameGrid.undoGridClick(*lastClick)
        self.clicks = self.clicks + 1
        self.drawGame()

    def switchView(self, nextView):
        """ change the active view """
        self.activeView = nextView

    def checkWin(self):
        if self.gameGrid == self.targetGrid:
            # You Won!
            self.stop()
