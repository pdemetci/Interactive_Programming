class EventManager:

    def __init__(self):
        """ create the event manager """
        pass

    def registerListener(self, listener):
        """ add a listener to the list of listeners; 
            the listener will be notified when an event occurs """
        pass

    def unregisterListener(self, listener):
        """ remove a listener from the list of listeners;
            the listener will no longer receive notifications """
        pass

    def post(self, event):
        """ send an event notification to all listeners """
        pass
