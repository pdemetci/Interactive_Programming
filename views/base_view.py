class BaseView:
    
    def __init__(self):
        """ setup the view """

    def draw(self, surface):
        """ draw the view """

    def setEventManager(self, eventManager):
        self.eventManager = eventManager
        self.eventManager.registerListener(self)

    def removeEventManager(self):
        self.eventManager.unregisterListener(self)
        self.eventManager = None

    def notify(self, event):
        """ update the view based on the event """
