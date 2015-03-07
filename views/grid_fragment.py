import pygame
from base_fragment import BaseFragment

class GridFragment(BaseFragment):
    CELL_BORDER = 4
    BORDER_COLOR = pygame.Color("black")

    colorDict = {
                    0: pygame.Color("white"),
                    1: pygame.Color("red"),
                    2: pygame.Color("orange"),
                    3: pygame.Color("yellow"),
                    4: pygame.Color("green"),
                    5: pygame.Color("blue"),
                    6: pygame.Color("purple")
    }

    def draw(self, surface, grid, cellGrid):
        """ draws the target grid """
        for row in range(grid.rows):
            for col in range(grid.cols):
                val = grid.get(row, col)
                cell = cellGrid.getCellRect(row, col)
                self.drawCell(surface, val, cell)

        pygame.display.update()

    def drawCell(self, surface, val, rect):
        color = self.getColor(val)
        surface.fill(color, rect)
        pygame.draw.rect(surface, self.BORDER_COLOR, rect, self.CELL_BORDER)

    def getColor(self, colorVal):
        return self.colorDict[colorVal]
     
