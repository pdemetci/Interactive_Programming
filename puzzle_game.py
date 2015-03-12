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
    TARGET_CLICKS = 4

    def __init__(self):
        """ create the view and controllers """

        # setup the controllers
        self.mouseController = MouseController(self)
        self.videoController = VideoController(self)
        self.gameStateController = GameStateController(self)
        self.menuController = MenuController(self)
        self.controllers = [self.mouseController,
                            self.videoController,
                            self.gameStateController,
                            self.menuController]

        # setup the models
        self.gameGrid = None
        self.targetGrid = None
        self.clicks = None
        self.clickHistory = None

        # setup the views
        self.gameView = GameView()
        self.menuView = MenuView()
        self.howtoView = HowtoView()
        self.activeView = None

        self.surface = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT), pygame.RESIZABLE)

    def start(self):
        """ start the game """

        # generate new game and target grids
        self.gameGrid = GameGrid(self.ROWS, self.COLS)
        self.targetGrid = TargetGrid(self.ROWS, self.COLS, self.TARGET_CLICKS)

        # clear the click history
        self.clicks = self.MAX_CLICKS
        self.clickHistory = []

        # start the game
        self.gameStateController.start()

        # make the menuView active
        self.switchView(self.menuView)
        self.drawGame()

        # run the main loop
        while not self.gameStateController.done:
            self.main()
            pygame.time.wait(50)

    def stop(self):
        """ stop the game """
        self.gameStateController.stop()

    def drawGame(self):
        """ draw the game """
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
        """ determine if the game is over """
        if self.gameGrid == self.targetGrid:
            # You Won!
            pygame.time.wait(1000)
            self.start()
