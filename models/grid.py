class Grid(object):
	def __init__(self, rows, cols):
		""" create a grid with a given number of rowsand columns """
		self.rows = rows
		self.cols = cols
		self.matrix = []

		b=[]
		for x in range(cols):
			b.append(0)	
		for i in range(rows):
			self.matrix.append(b)


	def get(self, row, col):
		""" get the value at a given row and column """
		return self.matrix[row][col]

	def set(self, row, col, val):
		""" set the cell at the row and column to val """
		self.matrix[row][col] = val
