from grid import Grid

class ClickGrid(Grid):
    """ the click grid manages a clickable grid """
    MAX_VALUES = 7

    def __init__(self, row, col):
        super(ClickGrid, self).__init__(row, col)

    def handleGridClick(self, row, col):
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
