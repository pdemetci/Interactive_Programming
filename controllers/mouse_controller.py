import base_controller

class MouseController(BaseController):
    
    def __init__(self, eventManager):
        """ create the mouse controller """
        self.eventManager = eventManager

    def notify(self, event):
        """ respond to events """
        if event.type == ClickEvent:
            x = event.x
            y = event.y
            gameCellGrid = event.gameCellGrid
            row, col = gameCellGrid.getRowCol(x, y)

            nextEvent = ClickEvent("GridClickEvent", row, col)

        if nextEvent:
            self.eventManager.post(nextEvent)
