class PuzzleGame:
    GAME_WIDTH = 1200
    GAME_HEIGHT = 600

    def __init__(self):
        """ create the view and controllers """
        self.done = True
        self.eventManager = EventManager()
        self.gameGrid = GameGrid(eventManager)
        self.targetGrid = TargetGrid(eventManager)
        self.gameView = GameView(eventManager)

    def start(self):
        """ start the game """
        self.done = False
        self.surface = pygame.display.set_mode(GAME_WIDTH, GAME_HEIGHT)
        while not done:
            main()

    def stop(self):
        """ stop the game """
        self.done = True

    def main(self):
        """ body of the main loop """
        for event in pygame.events.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                gameCellGrid = self.gameView.getGameCellGrid(self.surface, self.gameGrid)
                clickEvent = ClickEvent(x, y, gameCellGrid)


    def notify(self, event):
        """ respond to events """

    def switchView(nextView):
        """ change the active view """
