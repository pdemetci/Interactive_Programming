import base_event

class ClickEvent(BaseEvent):
    
    def __init__(self, row, col):
        """ create click event """ 
