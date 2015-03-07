from grid import Grid

class TargetGrid(Grid):
    """ the target grid represents the goal state of the game grid """

    def __init__(self, row, col):
        """ create the target grid """
    	self.row = row
    	self.col = col
    	self.grid= Grid(self.row,self.col)
    	self.fill_grid()

    def fill_grid(self):

    def fill_grid(self, grid):
        """ fills the grid with the a random target state """
    	for i in range(self.row):
    		for x in range(self.col):
    			self.grid.set(i,x,2)
