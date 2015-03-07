from base_event import BaseEvent

class ChangeCellEvent(BaseEvent):

    def __init__(self, row, col):
        print "should change cell:", row, col
        self.row = row
        self.col = col
