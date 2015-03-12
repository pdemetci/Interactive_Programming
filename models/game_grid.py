from click_grid import ClickGrid

class GameGrid(ClickGrid):
    """ the game grid manages a grid """

    def undoGridClick(self, row, col):
        """ undo a click at a given location """
        cells = self.getChangedCells(row, col)
        for cell in cells:
            self.decrementCell(*cell)

    def decrementCell(self, row, col):
        """ decrement the value of a cell by one """
        prevVal = self.get(row, col)
        nextVal = (prevVal - 1) % self.MAX_VALUES
        self.set(row, col, nextVal)
