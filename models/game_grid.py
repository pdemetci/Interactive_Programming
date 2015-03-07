from grid import Grid

class GameGrid(Grid):
    """ the game grid manages a grid based on events """

    def notify(self, event):
        """ respond to events """
        if event.type == ChangeCellEvent:
            row = event.row
            col = event.col
