from grid import Grid
from render_event import RenderEvent
from change_cell_event import ChangeCellEvent

class GameGrid(Grid):
    """ the game grid manages a grid based on events """

    def handleClick(self, row, col):
        cells = self.getChangedCells(row, col)
        for cell in cells:
            self.incrementCell(*cell)

    def getChangedCells(self, row, col):
        cells = []
        cells.append((row, col))
        cells.append((row - 1, col))
        cells.append((row + 1, col))
        cells.append((row, col - 1))
        cells.append((row, col + 1))

        return filter(lambda rc: self.inBounds(*rc), cells)

    def incrementCell(self, row, col):
        prevVal = self.get(row, col)
        nextVal = (prevVal + 1) % self.MAX_VALUES
        self.set(row, col, nextVal)

    def notify(self, event):
        """ respond to events """
        nextEvent = None
        if type(event) is ChangeCellEvent:
            row = event.row
            col = event.col

            self.handleClick(row, col)

            nextEvent = RenderEvent()

        if nextEvent:
            self.eventManager.post(nextEvent)
