from base_event import BaseEvent

class ClickEvent(BaseEvent):
    
    def __init__(self, x, y, clicksLeft):
        self.x = x
        self.y = y
        self.clicksLeft = clicksLeft
