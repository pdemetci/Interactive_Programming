import pygame

from event_manager import EventManager
from game_grid import GameGrid
from target_grid import TargetGrid
from game_view import GameView
from menu_view import MenuView
from event_manager import EventManager
from click_event import ClickEvent
from render_event import RenderEvent
from get_grid_click_event import GetGridClickEvent
from draw_game_event import DrawGameEvent
from grid_click_event import GridClickEvent

class PuzzleGame:
    GAME_WIDTH = 1200
    GAME_HEIGHT = 600

    ROWS = 5
    COLS = 5

    def __init__(self):
        """ create the view and controllers """
        self.done = True
        self.eventManager = EventManager()
        self.eventManager.registerListener(self)

        self.gameGrid = GameGrid(self.eventManager, self.ROWS, self.COLS)
        self.targetGrid = TargetGrid(self.eventManager, self.ROWS, self.COLS)

        self.gameView = GameView()
        self.menuView = MenuView()
        self.activeView = None
        self.surface = None

    def start(self):
        """ start the game """
        self.done = False
        self.switchView(self.gameView)
        self.surface = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.eventManager.post(RenderEvent())

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
                clickEvent = ClickEvent(x, y)
                self.eventManager.post(clickEvent)


    def notify(self, event):
        """ respond to events """
        nextEvent = None
        if type(event) is RenderEvent:
            surface = self.surface
            gameGrid = self.gameGrid
            targetGrid = self.targetGrid
            nextEvent = DrawGameEvent(surface, gameGrid, targetGrid)

        elif type(event) is GetGridClickEvent:
            surface = self.surface
            gameGrid = self.gameGrid
            nextEvent = GridClickEvent(surface, gameGrid, event.x, event.y)

        if nextEvent:
            self.eventManager.post(nextEvent)
            

    def switchView(self, nextView):
        """ change the active view """
        if self.activeView:
            self.activeView.removeEventManager()
        self.activeView = nextView
        self.activeView.setEventManager(self.eventManager)
