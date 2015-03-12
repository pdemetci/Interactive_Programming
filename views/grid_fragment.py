import pygame
from base_fragment import BaseFragment

class GridFragment(BaseFragment):
    CELL_BORDER = 4
    BORDER_COLOR = pygame.Color("black")

    colorDict = {
                    0: pygame.Color("white"),
                    1: pygame.Color("red"),
                    2: pygame.Color("orange"),
                    3: pygame.Color("green"),
                    4: pygame.Color("blue"),
                    5: pygame.Color("purple"),
                    6: pygame.Color("black")
    }

    def draw(self, surface, grid, gridSizer):
        """ draws the target grid """
        for row in range(grid.rows):
            for col in range(grid.cols):
                val = grid.get(row, col)
                cell = gridSizer.getCellRect(row, col)
                self.drawCell(surface, val, cell)

    def drawCell(self, surface, val, rect):
        color = self.getColor(val)
        surface.fill(color, rect)
        pygame.draw.rect(surface, self.BORDER_COLOR, rect, self.CELL_BORDER)

    def getColor(self, colorVal):
        return self.colorDict[colorVal]
     
