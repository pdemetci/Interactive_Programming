from grid_fragment import GridFragment

class GameGridFragment(GridFragment):

    def notify(self, event):
        """ handle events """
        if isinstance(event, ClickEvent):
            pixelX = event.x
            pixelY = event.y
            cellGrid = event.cellGrid

            row, col = cellGrid.getRowCol(pixelX, pixelY)
            nextEvent = GridClickEvent(row, col)

        if nextEvent:
            eventManager.post(nextEvent)
