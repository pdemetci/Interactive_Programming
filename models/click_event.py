from base_event import BaseEvent

class ClickEvent(BaseEvent):
    
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
