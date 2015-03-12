from random import randint
from click_grid import ClickGrid

class TargetGrid(ClickGrid):
    """ the target grid represents the goal state of the game grid """

    def __init__(self, row, col, clicks):
        """ create the target grid """
        super(TargetGrid, self).__init__(row, col)
        self.clicks = clicks
    	self.fillGrid(clicks)

    def fillGrid(self, clicks):
        """ fills the grid with the a random target state """
        for i in range(clicks):
            row, col = self.getRandRowCol()
            self.handleGridClick(row, col)

    def getRandRowCol(self):
        """ gets a random row, column tuple in the grid's bounds """
        row = randint(0, self.rows - 1)
        col = randint(0, self.cols - 1) 
        return (row, col)
