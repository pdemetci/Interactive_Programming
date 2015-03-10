from click_grid import ClickGrid

class GameGrid(ClickGrid):
    """ the game grid manages a grid """
    MAX_VALUES = 7

    def undoGridClick(self, row, col):
        cells = self.getChangedCells(row, col)
        for cell in cells:
            self.decrementCell(*cell)

    def decrementCell(self, row, col):
        prevVal = self.get(row, col)
        nextVal = (prevVal - 1) % self.MAX_VALUES
        self.set(row, col, nextVal)
