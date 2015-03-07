from grid import Grid

class TargetGrid(Grid):
    """ the target grid represents the goal state of the game grid """

    def __init__(self, row, col):
        """ create the target grid """
        super(TargetGrid, self).__init__(row, col)
    	self.fill_grid()

    def fill_grid(self):
        """ fills the grid with the a random target state """
    	for i in range(self.rows):
    		for x in range(self.cols):
    			self.set(i,x,2)

    def notify(self, event):
        """ handle events """
