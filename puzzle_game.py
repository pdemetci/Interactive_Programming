import pygame
from game_grid import GameGrid
from target_grid import TargetGrid
from game_view import GameView
from menu_view import MenuView
from game_grid_sizer import GameGridSizer
from mouse_controller import MouseController
from video_controller import VideoController
from game_state_controller import GameStateController
from menu_controller import MenuController
from howto_view import HowtoView

class PuzzleGame:
    GAME_WIDTH = 1200
    GAME_HEIGHT = 720

    ROWS = 5
    COLS = 5

    MAX_CLICKS = 10

    def __init__(self):
        """ create the view and controllers """
        self.mouseController = MouseController(self)
        self.videoController = VideoController(self)
        self.gameStateController = GameStateController(self)
        self.menuController = MenuController(self)
        self.controllers = [self.mouseController,
                            self.videoController,
                            self.gameStateController,
                            self.menuController]

        self.gameGrid = None
        self.targetGrid = None
        self.clicks = self.MAX_CLICKS
        self.clickHistory = []

        self.gameView = GameView()
        self.menuView = MenuView()
        self.howtoView = HowtoView()
        self.activeView = None

        self.surface = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT), pygame.RESIZABLE)

    def start(self):
        """ start the game """
        self.gameGrid = GameGrid(self.ROWS, self.COLS)
        self.targetGrid = TargetGrid(self.ROWS, self.COLS, 3)
        self.gameStateController.start()
        self.switchView(self.menuView)
        self.drawGame()

        while not self.gameStateController.done:
            self.main()
            pygame.time.wait(50)

    def stop(self):
        self.gameStateController.stop()

    def drawGame(self):
        self.activeView.draw(self)

    def main(self):
        """ body of the main loop """
        for event in pygame.event.get():
            for controller in self.controllers:
                controller.handleEvent(event)

    def switchView(self, nextView):
        """ change the active view """
        self.activeView = nextView

    def checkWin(self):
        if self.gameGrid == self.targetGrid:
            # You Won!
            pygame.time.wait(1000)
            self.start()
