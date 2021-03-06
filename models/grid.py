class Grid(object):
	def __init__(self, rows, cols):
		""" create a grid with a given number of rowsand columns """
		self.rows = rows
		self.cols = cols
		self.matrix = [[0 for c in range(cols)] for r in range(rows)]

	def inBounds(self, row, col):
		""" check if row and col are within the grid """
		return row >= 0 and row < self.rows and col >= 0 and col < self.cols

	def get(self, row, col):
		""" get the value at a given row and column """
		return self.matrix[row][col]

	def set(self, row, col, val):
		""" set the cell at the row and column to val """
		self.matrix[row][col] = val

	def __eq__(self, other):
		""" determine if two grids are equal """
		return isinstance(self, Grid) and self.matrix == other.matrix

	def __ne__(self, other):
		""" determine if two grids are not equal """ 
		return not self.__eq__(other)

	def __str__(self):
		""" convert the grid to string """
		return str(self.matrix)
