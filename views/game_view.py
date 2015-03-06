from base_view import BaseView

class GameView(BaseView):

    def __init__(self, eventManager):
        """ creates the game view """
        self.eventManager = eventManager
        self.gameGridFragment = GameGridFragment(eventManager)
        self.targetGridFragment = TargetGridFragment(eventManager)

        eventManager.registerListener(self)

    def draw(self, surface, gameGrid, targetGrid):
        """ draw the game grid and target grid """
        gameCellGrid = getGameCellGrid(surface, gameGrid)
        targetCellGrid = getTargetCellGrid(surface, targetGrid)

        self.gameGridFragment.draw(surface, gameGrid, gameCellGrid)
        self.targetGridFragment.draw(surface, targetGrid, targetCellGrid)

    def notify(self, event):
        if event.type == DrawEvent:
            gameGrid = event.gameGrid
            targetGrid = event.targetGrid
            surface = event.surface

            self.draw(surface, gameGrid, targetGrid)

    def getGameCellGrid(surface, gameGrid):
        """ gets a rectangular portion of the surface """
        sufaceWidth, surfaceHeight = surface.get_size()

        gridX = surfaceWidth / 2.0
        gridY = 0
        gridWidth = surfaceWidth / 2.0
        gridHeight = surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return CellGrid(gameGrid.rows, gameGrid.cols, boundsRect)
        
    def getTargetCellGrid(surface, targetGrid):
        """ gets a rectangular portion of the surface """
        sufaceWidth, surfaceHeight = surface.get_size()

        gridX = 0
        gridY = 0
        gridWidth = surfaceWidth / 2.0
        gridHeight = surfaceHeight

        boundsRect = pygame.Rect(gridX, gridY, gridWidth, gridHeight)
        return CellGrid(targetGrid.rows, targetGrid.cols, boundsRect)
        
