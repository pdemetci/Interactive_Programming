class CellGrid:
    
    def __init__(rows, cols, boundsRect):
        """ create the cell grid """
        self.rows = rows
        self.cols = cols
        self.rect = boundsRect

        self.width = boundsRect.width
        self.height = boundsRect.height

        self.cellWidth = self.width / float(self.cols)
        self.cellHeight = self.height / float(self.rows)

    def getCellRect(row, col):
        """ gets the rect for a cell """
        x0, y0 = self.rect.topleft
        cellX0 = x0 + (col * self.cellWidth)
        cellY0 = y0 + (row * self.cellHeight)

        return pygame.Rect(cellX0, cellY0, cellWidth, cellHeight)

    def getRowCol(pixelX, pixelY):
        x0, y0 = self.rect.topleft
        relX = pixelX - x0
        relY = pixelY - y0

        row = int(relY / self.cellHeight)
        col = int(relX / self.cellWidth)

        return (row, col)


