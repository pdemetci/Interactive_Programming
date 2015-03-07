class EventManager:

    def __init__(self):
        """ create the event manager """
        self.listeners = []

    def registerListener(self, listener):
        """ add a listener to the list of listeners; 
            the listener will be notified when an event occurs """
        self.listeners.append(listener)

    def unregisterListener(self, listener):
        """ remove a listener from the list of listeners;
            the listener will no longer receive notifications """
        self.listeners.remove(listener)

    def post(self, event):
        """ send an event notification to all listeners """
        for listener in self.listeners:
            print event, "--->", listener
            listener.notify(event)

