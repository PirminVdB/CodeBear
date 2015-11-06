__author__ = 'PirminVDB'

class Model():
    def __init__(self):
        self.change_listeners = dict()
        self.change_event = ChangeEvent(self)

    def add_change_listener(self, change_listener):
        self.listeners[change_listener.__class__] = change_listener

    def remove_change_listener(self, change_listener):
        del self.change_listeners[change_listener.__class__]

    def _fire_state_changed(self):
        for change_listener in self.change_listeners.values():
            change_listener.state_changed(self.change_event)

'''
ChangeEvent is used to notify interested parties that state has changed in the event source.
http://docs.oracle.com/javase/7/docs/api/javax/swing/event/ChangeEvent.html
'''
class ChangeEvent():
    def __init__(self, model):
        self.model = model

    def get_model(self):
        return self.model

'''
Defines an object which listens for ChangeEvents.
http://docs.oracle.com/javase/7/docs/api/javax/swing/event/ChangeListener.html#stateChanged%28javax.swing.event.ChangeEvent%29
'''
class ChangeListener():
    def state_changed(self, change_event):
        pass