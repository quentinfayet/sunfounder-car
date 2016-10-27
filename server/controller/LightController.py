from observable import Observer
from event import Event

class LightController(Observer):
    def handle(self, event):
        print('Received ', event.get_value())
        response = Event('light controller')
        event.respond_to_emmiter(response)
