from grid import Grid

class ClickGrid(Grid):
	""" the click grid manages a clickable grid """

	MAX_VALUES = 7

	def handleGridClick(self, row, col):
		""" handle a click input """
		cells = self.getChangedCells(row, col)
		for cell in cells:
			self.incrementCell(*cell)

	def getChangedCells(self, row, col):
		""" determine which cells should be changed """

        # add the five cells in a cross formation
		cells = []
		cells.append((row, col))
		cells.append((row - 1, col))
		cells.append((row + 1, col))
		cells.append((row, col - 1))
		cells.append((row, col + 1))

        # remove any cells that are out bounds
		return filter(lambda rc: self.inBounds(*rc), cells)

	def incrementCell(self, row, col):
		""" increment the value of a cell by one """
		prevVal = self.get(row, col)
		nextVal = (prevVal + 1) % self.MAX_VALUES
		self.set(row, col, nextVal)
