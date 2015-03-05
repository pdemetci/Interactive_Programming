class EventManager:

    def __init__(self):
        """ create the event manager """

    def registerListener(self, listener):
        """ add a listener to the list of listeners; 
            the listener will be notified when an event occurs """

    def unregisterListener(self, listener):
        """ remove a listener from the list of listeners;
            the listener will no longer receive notifications """

    def post(self, event):
        """ send an event notification to all listeners """
