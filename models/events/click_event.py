from base_event import BaseEvent

class ClickEvent(BaseEvent):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
