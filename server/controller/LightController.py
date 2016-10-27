from observable import Observer
from event import Event
import RPi.GPIO as GPIO


class LightController(Observer):

    _gpios = None

    def __init__(self):
        self._gpios = {
            'red': 11,
            'green': 12,
            'blue': 13,
        }

    def handle(self, event):
        event_value = event.get_value()

        if event_value['component'] != 'light':
            return

        #TODO : Add 'command' existence checking

        if event_value['command'] == 'setColor':
            self.setColor(event_value)


    def setColor(self, event_value):
        pass
