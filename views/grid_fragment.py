from base_fragment import BaseFragment

class GridFragment(BaseFragment):
    CELL_BORDER = 2

    colorDict = {
                    1: pygame.Color("red"),
                    2: pygame.Color("orange"),
                    3: pygame.Color("yellow"),
                    4: pygame.Color("green"),
                    5: pygame.Color("blue"),
                    6: pygame.Color("purple")
    }

    def draw(self, surface, grid, cellGrid):
        """ draws the target grid """
        for row in grid.rows:
            for col in cols:
                val = grid.get(row, col)
                cell = cellGrid.getCellRect(row, col)
                drawRect(surface, val, cell)

    def drawCell(surface, val, rect):
        color = getColor(val)
        pygame.draw.rect(surface, color, rect, CELL_BORDER)

    def getColor(colorVal):
        return colorDict[colorVal]
     
