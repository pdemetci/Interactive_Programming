import pygame

class GridSizer(object):
    
    def __init__(self, rows, cols, boundsRect):
        """ create the cell grid """
        self.rows = rows
        self.cols = cols
        self.rect = boundsRect

        self.width = boundsRect.width
        self.height = boundsRect.height

        self.cellWidth = self.width / float(self.cols)
        self.cellHeight = self.height / float(self.rows)

    def getCellRect(self, row, col):
        """ gets the rect for a cell """
        x0, y0 = self.rect.topleft
        cellX0 = x0 + (col * self.cellWidth)
        cellY0 = y0 + (row * self.cellHeight)

        return pygame.Rect(cellX0, cellY0, self.cellWidth, self.cellHeight)

    def getRowCol(self, pixelX, pixelY):
        x0, y0 = self.rect.topleft

        if self.outOfBounds(pixelX, pixelY):
            return None

        relX = pixelX - x0
        relY = pixelY - y0

        row = int(relY / self.cellHeight)
        col = int(relX / self.cellWidth)

        return (row, col)

    def outOfBounds(self, px, py):
        return not self.rect.collidepoint(px, py)
